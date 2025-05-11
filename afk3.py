from .. import loader, utils
import time
import asyncio
import random
from datetime import datetime, timedelta
from telethon.tl.types import Message

@loader.tds
class AfkChatGPTMod(loader.Module):
    """AFK режим с настройкой времени и кастомными ответами"""
    strings = {
        "name": "@YMEPOTBAC АФК режимы",
        "afk_on": "🟢 <b>AFK режим включен</b>\nПричина: {reason}\nВернусь примерно в: {return_time}",
        "afk_off": "🔴 <b>AFK режим выключен</b>\nБыл неактивен: {time}",
        "afk_response": "<b>{response}</b>\n\nВернусь примерно в {return_time}",
        "default_reason": "использую автоотвечик для ответов",
        "afk_time_error": "❌ <b>Неверный формат времени!</b>\nИспользуйте: <code>.afk (причина) (время, например 18:30)</code>",
        "afksms_set": "✅ <b>Установлен кастомный ответ:</b>\n<code>{response}</code>",
        "afksms_reset": "✅ <b>Кастомный ответ сброшен на стандартный</b>"
    }

    def __init__(self):
        self.afk = False
        self.start_time = None
        self.reason = ""
        self.return_time = None
        self.custom_response = None
        self.gpt_cache = {}

    async def client_ready(self, client, db):
        self.client = client

    async def afkcmd(self, message):
        """Включить AFK с причиной и временем возврата | .afk (причина) (время, например 18:30)"""
        args = utils.get_args_raw(message)
        
        if self.afk:
            # Выключаем AFK режим
            afk_duration = str(datetime.now() - self.start_time).split('.')[0]
            await utils.answer(message, self.strings["afk_off"].format(time=afk_duration))
            self.afk = False
            return
        
        # Включаем AFK режим
        if not args:
            self.reason = self.strings["default_reason"]
            self.return_time = (datetime.now() + timedelta(hours=2)).strftime("%H:%M")
        else:
            # Парсим причину и время
            parts = args.split(maxsplit=1)
            if len(parts) == 1:
                self.reason = parts[0]
                self.return_time = (datetime.now() + timedelta(hours=2)).strftime("%H:%M")
            else:
                reason_part, time_part = parts
                try:
                    # Проверяем, есть ли время в формате HH:MM
                    if ":" in time_part:
                        hours, minutes = map(int, time_part.split(":"))
                        if hours < 0 or hours > 23 or minutes < 0 or minutes > 59:
                            raise ValueError
                        now = datetime.now()
                        return_time = now.replace(hour=hours, minute=minutes, second=0)
                        if return_time < now:
                            return_time += timedelta(days=1)  # Если время уже прошло, переносим на завтра
                        self.return_time = return_time.strftime("%H:%M")
                        self.reason = reason_part
                    else:
                        self.reason = args
                        self.return_time = (datetime.now() + timedelta(hours=2)).strftime("%H:%M")
                except (ValueError, IndexError):
                    await utils.answer(message, self.strings["afk_time_error"])
                    return

        self.start_time = datetime.now()
        self.afk = True
        await utils.answer(
            message,
            self.strings["afk_on"].format(
                reason=self.reason,
                return_time=self.return_time
            )
        )

    async def afksmscmd(self, message):
        """Установить кастомный ответ для AFK | .afksms (текст) или .afksms без текста для сброса"""
        args = utils.get_args_raw(message)
        
        if not args:
            self.custom_response = None
            await utils.answer(message, self.strings["afksms_reset"])
        else:
            self.custom_response = args
            await utils.answer(message, self.strings["afksms_set"].format(response=args))

    async def watcher(self, message):
        if not self.afk:
            return

        if not getattr(message, "out", False) and isinstance(message, Message) and getattr(message, "raw_text", ""):
            text = message.raw_text
            
            if text in self.gpt_cache:
                response = self.gpt_cache[text]
            else:
                response = await self.generate_gpt_response(text)
                self.gpt_cache[text] = response

            await utils.answer(
                message,
                self.strings["afk_response"].format(
                    response=response,
                    return_time=self.return_time
                )
            )

    async def generate_gpt_response(self, text):
        """Генерация ответа (кастомный или рандомный)"""
        if self.custom_response:
            return self.custom_response
        
        responses = [
            "Я сейчас недоступен, но вы можете оставить сообщение и я позже отвечу!",
            "Извините, я не у телефона.",
            "Занят, отвечу через час.",
            "Ожидайте ответа в течении часа.",
            "Сообщение принято! Ожидайте ответа.",
            "Я в АФК режиме. Ожидайте",
            "Спасибо за сообщение! Отвечу позже.",
            "Автоматический ответ: я вас услышал, отвечу при первой возможности!",
            "Сейчас не могу ответить, но обязательно прочту ваше сообщение позже."
        ]
        await asyncio.sleep(1)  # Имитация задержки API
        return random.choice(responses)