from .. import loader, utils
import time
import asyncio
import random
from datetime import datetime, timedelta
from telethon.tl.types import Message

@loader.tds
class AfkChatGPTMod(loader.Module):
    """AFK режим с ответами через автоотвечика"""
    strings = {
        "name": "@YMEPOTBAC АФК режимы",
        "afk_on": "🟢 <b>AFK режим включен</b>\nПричина: {reason}",
        "afk_off": "🔴 <b>AFK режим выключен</b>\nБыл неактивен: {time}",
        "afk_response": "🤖 <b>Автоответчик (AFK режим)</b>\n{response}\n\n<i>Вернусь примерно в {return_time}</i>",
        "default_reason": "Занят, немогу ответить"
    }

    def __init__(self):
        self.afk = False
        self.start_time = None
        self.reason = ""
        self.gpt_cache = {}

    async def client_ready(self, client, db):
        self.client = client

    async def afkcmd(self, message):
        """Включить/выключить AFK режим"""
        if self.afk:
            # Выключаем AFK режим
            afk_time = str(datetime.now() - self.start_time).split('.')[0]
            await utils.answer(message, self.strings["afk_off"].format(time=afk_time))
            self.afk = False
        else:
            # Включаем AFK режим
            args = utils.get_args_raw(message)
            self.reason = args if args else self.strings["default_reason"]
            self.start_time = datetime.now()
            self.afk = True
            await utils.answer(message, self.strings["afk_on"].format(reason=self.reason))

    async def watcher(self, message):
        if not self.afk:
            return

        # Проверяем, что сообщение не исходящее и является текстовым
        if not getattr(message, "out", False) and isinstance(message, Message) and getattr(message, "raw_text", ""):
            # Получаем текст сообщения
            text = message.raw_text
            
            # Генерируем ответ через ChatGPT (имитация)
            if text in self.gpt_cache:
                response = self.gpt_cache[text]
            else:
                response = await self.generate_gpt_response(text)
                self.gpt_cache[text] = response

            # Форматируем время возвращения
            return_time = (self.start_time + timedelta(hours=2)).strftime("%H:%M")
            
            # Отправляем ответ
            await utils.answer(
                message,
                self.strings["afk_response"].format(
                    response=response,
                    return_time=return_time
                )
            )

    async def generate_gpt_response(self, text):
        """Автоответчик с рандомными ответами"""
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