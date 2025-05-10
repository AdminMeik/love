# meta developer: @YMEPOTBAC

import asyncio
from .. import loader, utils
from telethon.errors import MessageNotModifiedError

@loader.tds
class RomanovaMod(loader.Module):
    """Модуль с эффектом печатания текста про Катю Романову"""

    strings = {
        "name": "@YMEPOTBAC Романова",
        "not_subscribed": "<b>Для использования этой команды необходимо подписаться на канал</b>",
    }

    def __init__(self):
        self.name = self.strings["name"]
        self._me = None
        self.text_frames = [
            "К",
            "Ка",
            "Кат",
            "Катя",
            "Катя ",
            "Катя Р",
            "Катя Ро",
            "Катя Ром",
            "Катя Рома",
            "Катя Роман",
            "Катя Романова",
            "Катя Романова ",
            "Катя Романова п",
            "Катя Романова по",
            "Катя Романова пор",
            "Катя Романова пора",
            "Катя Романова пора ",
            "Катя Романова пора к",
            "Катя Романова пора ко",
            "Катя Романова пора коп",
            "Катя Романова пора копа",
            "Катя Романова пора копат",
            "Катя Романова пора копать",
            "Катя Романова пора копать ",
            "Катя Романова пора копать к",
            "Катя Романова пора копать ка",
            "Катя Романова пора копать кар",
            "Катя Романова пора копать карт",
            "Катя Романова пора копать карто",
            "Катя Романова пора копать картош",
            "Катя Романова пора копать картошк",
            "Катя Романова пора копать картошку",
            "Катя Романова пора копать картошку!",
            "Катя Романова пора копать картошку!!",
            "Катя Романова пора копать картошку!!!",
        ]

    async def client_ready(self, client, db):
        self.client = client
        self.db = db
        self.is_ready = True

    @loader.command(ru_doc="Эффект печатания текста про Катю Романову")
    async def romanova(self, message):
        """Эффект печатания текста"""
        try:
            is_subscribed = True  # Можно добавить проверку подписки

            if not is_subscribed:
                await utils.answer(message, self.strings["not_subscribed"])
                return

            for frame in self.text_frames:
                try:
                    await utils.answer(message, frame)
                    await asyncio.sleep(0.15)  # Быстрая печать
                except MessageNotModifiedError:
                    pass
            
            # Добавляем мигание в конце
            for _ in range(3):
                try:
                    await utils.answer(message, "Катя Романова пора копать картошку!!!")
                    await asyncio.sleep(0.5)
                    await utils.answer(message, "Катя Романова пора копать картошку   ")
                    await asyncio.sleep(0.2)
                except MessageNotModifiedError:
                    pass

        except Exception as e:
            print(f"Ошибка в анимации: {e}")