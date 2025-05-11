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
        "name": "@YMEPOTBAC Любовь 2",
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

        self.love_phrases = [
            "Я тебя люблю",  # Русский
            "I love you",    # Английский
            "Je t'aime",     # Французский
            "Ich liebe dich", # Немецкий
            "Ti amo",        # Итальянский
            "Te quiero",     # Испанский
            "愛してる",       # Японский
            "사랑해",         # Корейский
            "我爱你",        # Китайский
            "أحبك",          # Арабский
            "Σ'αγαπώ",       # Греческий
            "Ik hou van jou", # Голландский
            "Eu te amo",    # Португальский
            "Jag älskar dig", # Шведский
            "Miluji tě",     # Чешский
            "Volim te",      # Хорватский
            "Szeretlek",    # Венгерский
            "Kocham cię",    # Польский
            "Te iubesc",     # Румынский
            "Mahal kita",    # Филиппинский
            "ฉันรักคุณ",      # Тайский
            "Tôi yêu bạn",   # Вьетнамский
            "Я тебя кахаю",  # Белорусский
            "Я тебе кохаю",  # Украинский
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

    @loader.command(ru_doc="анимация с летающими сердечками.")
    async def love2(self, message):
        """анимация с летающими сердечками."""
        try:
            is_subscribed = True

            if not is_subscribed:
                await utils.answer(message, self.strings["not_subscribed"])
                return

            frames = [
                "💖\n\n\n\n\n\n\n",
                "\n💖\n\n\n\n\n\n",
                "\n\n💖\n\n\n\n\n",
                "\n\n\n💖\n\n\n\n",
                "\n\n\n\n💖\n\n\n",
                "\n\n\n\n\n💖\n\n",
                "\n\n\n\n\n\n💖\n",
                "\n\n\n\n\n\n\n💖",
                "\n\n\n\n\n\n💖\n",
                "\n\n\n\n\n💖\n\n",
                "\n\n\n\n💖\n\n\n",
                "\n\n\n💖\n\n\n\n",
                "\n\n💖\n\n\n\n\n",
                "\n💖\n\n\n\n\n\n",
                "💖\n\n\n\n\n\n\n",
                "❤️ ЛЮБОВЬ ❤️"
            ]

            for frame in frames:
                try:
                    await utils.answer(message, frame)
                    await asyncio.sleep(0.2)
                except MessageNotModifiedError:
                    pass
        except Exception as e:
            print(f"ошибка анимации love2: {e}")

    @loader.command(ru_doc="рулетка сердечек с рандомным выпаданием.")
    async def love3(self, message):
        """рулетка сердечек с рандомным выпаданием."""
        try:
            is_subscribed = True

            if not is_subscribed:
                await utils.answer(message, self.strings["not_subscribed"])
                return

            hearts = ["❤️", "💛", "💚", "💙", "💜", "💕", "💞", "💓", "💗", "💖", "💘", "💝"]
            spinning = ["🌀", "🌪️", "⚡", "✨", "🌟"]
            
            # Анимация вращения
            for _ in range(5):
                spin_frame = random.choice(spinning)
                await utils.answer(message, spin_frame)
                await asyncio.sleep(0.3)
            
            # Результат
            result = random.choice(hearts)
            await utils.answer(message, f"Выпало: {result}")
        except Exception as e:
            print(f"ошибка рулетки love3: {e}")

    @loader.command(ru_doc="я тебя люблю на разных языках мира.")
    async def love4(self, message):
        """я тебя люблю на разных языках мира."""
        try:
            is_subscribed = True

            if not is_subscribed:
                await utils.answer(message, self.strings["not_subscribed"])
                return

            # Перемешиваем фразы для разнообразия
            shuffled_phrases = random.sample(self.love_phrases, len(self.love_phrases))
            
            for phrase in shuffled_phrases:
                try:
                    await utils.answer(message, phrase)
                    await asyncio.sleep(0.5)
                except MessageNotModifiedError:
                    pass
            
            # Завершающее сообщение
            await utils.answer(message, "❤️ Ты самый лучший! ❤️")
        except Exception as e:
            print(f"ошибка love4: {e}")