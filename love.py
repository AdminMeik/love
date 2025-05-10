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
        "name": "Любовь",
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
 

    async def client_ready(self, client, db):
        self.client = client
        self.db = db
        self.is_ready = True

    @loader.command(ru_doc="отображает анимированное сердечко.")
    async def love(self, message):
        """отображает анимированное сердечко."""
        try:
            # Проверяем, подписан ли пользователь на канал (замените на свой метод проверки)
            # try:
            #     user = await self.client.get_entity(message.sender_id)
            #     await self.client(GetParticipantRequest(
            #         channel=self.config["channel"],
            #         participant=user,
            #     ))
            # except Exception as e:
            #     await utils.answer(message, self.strings["not_subscribed"])
            #     return
            is_subscribed = True  # Заглушка, пока нет реальной проверки подписки

            if not is_subscribed:
                await utils.answer(message, self.strings["not_subscribed"])
                return

            for frame in self.heart_frames:
                try:
                    await utils.answer(message, f"<pre>{frame}</pre>")  # Оборачиваем frame в <pre> тег
                    await asyncio.sleep(0.25)  # asyncio.sleep для Hikka
                except MessageNotModifiedError:
                    pass
        except Exception as e:
            print(f"ошибка анимации сердечка: {e}")