# meta developer: @YMEPOTBAC

import asyncio
import random
from .. import loader, utils
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.errors import MessageNotModifiedError


@loader.tds
class HeartMod(loader.Module):
    """отображает анимированное сердечко дающие любовь."""

    strings = {
        "name": "@YMEPOTBAC Любовь 1",
        "not_subscribed": "<b>для использования этой команды необходимо подписаться на канал</b>",
    }

    def __init__(self):
        self.name = self.strings["name"]
        self._me = None
        self.heart_frames = [
            "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛🟫⬛🟫⬛⬛\n⬛🟫🟫🟫🟫🟫⬛\n⬛🟫🟫🟫🟫🟫⬛\n⬛⬛🟫🟫🟫⬛⬛\n⬛⬛⬛🟫⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛",
            "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛🟪⬛🟪⬛⬛\n⬛🟪🟪🟪🟪🟪⬛\n⬛🟪🟪🟪🟪🟪⬛\n⬛⬛🟪🟪🟪⬛⬛\n⬛⬛⬛🟪⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛",
            "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛🟦⬛🟦⬛⬛\n⬛🟦🟦🟦🟦🟦⬛\n⬛🟦🟦🟦🟦🟦⬛\n⬛⬛🟦🟦🟦⬛⬛\n⬛⬛⬛🟦⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛",
            "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛🟩⬛🟩⬛⬛\n⬛🟩🟩🟩🟩🟩⬛\n⬛🟩🟩🟩🟩🟩⬛\n⬛⬛🟩🟩🟩⬛⬛\n⬛⬛⬛🟩⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛",
            "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛🟨⬛🟨⬛⬛\n⬛🟨🟨🟨🟨🟨⬛\n⬛🟨🟨🟨🟨🟨⬛\n⬛⬛🟨🟨🟨⬛⬛\n⬛⬛⬛🟨⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛",
            "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛🟧⬛🟧⬛⬛\n⬛🟧🟧🟧🟧🟧⬛\n⬛🟧🟧🟧🟧🟧⬛\n⬛⬛🟧🟧🟧⬛⬛\n⬛⬛⬛🟧⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛",
            "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛🟥⬛🟥⬛⬛\n⬛🟥🟥🟥🟥🟥⬛\n⬛🟥🟥🟥🟥🟥⬛\n⬛⬛🟥🟥🟥⬛⬛\n⬛⬛⬛🟥⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛",
            "I",
            "I ",
            "I L",
            "I LO",
            "I LOV",
            "I LOVE",
            "I LOVE ",
            "I LOVE Y",
            "I LOVE YO",
            "I LOVE YOU",  ]
        
        self.heart_frames1 = [
            "❤️💛💚💙💜",
            "💜❤️💛💚💙",
            "💙💜❤️💛💚",
            "💚💙💜❤️💛",
            "💛💚💙💜❤️",
            "💕💞💓💗💖",
            "💖💕💞💓💗",
            "💗💖💕💞💓",
            "💓💗💖💕💞",
            "💞💓💗💖💕",
            "✨🌟💫⭐️🌠",
            "🌠✨🌟💫⭐️",
            "⭐️🌠✨🌟💫",
            "💫⭐️🌠✨🌟",
            "🌟💫⭐️🌠✨",
            "L",
            "LO",
            "LOV",
            "LOVE",
            "LOVE ",
            "LOVE Y",
            "LOVE YO",
            "LOVE YOU",
            "❤️ LOVE YOU ❤️"
        ]
 

    async def client_ready(self, client, db):
        self.client = client
        self.db = db
        self.is_ready = True

    @loader.command(ru_doc="отображает анимированное сердечко.")
    async def love(self, message):
        """отображает анимированное сердечко."""
        try:
            is_subscribed = True  # Заглушка, пока нет реальной проверки подписки

            if not is_subscribed:
                await utils.answer(message, self.strings["not_subscribed"])
                return

            for frame in self.heart_frames:
                try:
                    await utils.answer(message, f"<pre>{frame}</pre>")
                    await asyncio.sleep(0.25)
                except MessageNotModifiedError:
                    pass
        except Exception as e:
            print(f"ошибка анимации сердечка: {e}")

    @loader.command(ru_doc="альтернативная анимация сердечка с эмодзи.")
    async def love1(self, message):
        """альтернативная анимация сердечка с эмодзи."""
        try:
            is_subscribed = True  # Заглушка, пока нет реальной проверки подписки

            if not is_subscribed:
                await utils.answer(message, self.strings["not_subscribed"])
                return

            for frame in self.heart_frames1:
                try:
                    await utils.answer(message, frame)
                    await asyncio.sleep(0.3)
                except MessageNotModifiedError:
                    pass
        except Exception as e:
            print(f"ошибка анимации сердечка: {e}")
