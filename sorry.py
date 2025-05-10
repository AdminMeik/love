# meta developer: @YMEPOTBAC

import asyncio
from .. import loader, utils
from telethon.errors import MessageNotModifiedError

@loader.tds
class RomanticMessagesMod(loader.Module):
    """Романтические сообщения с 1001 розой и извинениями"""

    strings = {
        "name": "@YMEPOTBAC Извенения и подарок",
        "not_subscribed": "<b>Для использования этой команды необходимо подписаться на канал</b>",
    }

    def __init__(self):
        self.name = self.strings["name"]
        self._me = None

    async def client_ready(self, client, db):
        self.client = client
        self.db = db
        self.is_ready = True

    @loader.command(ru_doc="Показать 1001 розу")
    async def surprise(self, message):
        """Отправить 1001 розу"""
        try:
            is_subscribed = True  # Можно добавить проверку подписки

            if not is_subscribed:
                await utils.answer(message, self.strings["not_subscribed"])
                return

            # Отправляем сообщение о начале
            await utils.answer(message, "Готовлю 1001 розу для вас... ??")

            # Отправляем розы порциями по 100 штук
            roses = []
            for i in range(1, 1002):
                roses.append("??")
                if i % 100 == 0 or i == 1001:
                    await message.respond("".join(roses))
                    roses = []
                    await asyncio.sleep(0.5)

            # Финальное сообщение
            await message.respond("?? 1001 роза для тебя! ??")

        except Exception as e:
            print(f"Ошибка в команде surprise: {e}")

    @loader.command(ru_doc="1001 извинение")
    async def sorry(self, message):
        """Отправить 1001 извинение"""
        try:
            is_subscribed = True  # Можно добавить проверку подписки

            if not is_subscribed:
                await utils.answer(message, self.strings["not_subscribed"])
                return

            # Отправляем сообщение о начале
            msg = await utils.answer(message, "Готовлю 1001 извинение...")

            # Отправляем извинения порциями по 10 штук
            apologies = []
            for i in range(1, 1002):
                apology = f"Прости меня, я извиняюсь {i}/1001"
                apologies.append(apology)
                
                if i % 10 == 0 or i == 1001:
                    try:
                        await msg.edit("\n".join(apologies))
                    except MessageNotModifiedError:
                        pass
                    
                    if i != 1001:
                        await asyncio.sleep(1)
                    
                    if i % 100 == 0:
                        apologies = []  # Очищаем список чтобы не перегружать сообщение

            # Финальное сообщение
            await message.respond("Я искренне сожалею! ??")

        except Exception as e:
            print(f"Ошибка в команде sorry: {e}")