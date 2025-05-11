from .. import loader, utils
from asyncio import sleep
import random

@loader.tds
class PotatoMod(loader.Module):
    """Анимированная картошка на всех языках"""
    strings = {
        "name": "@YMEPOTBAC картошка на всех языках мира",
        "loading": "<i>Чищу картошечку...</i>",
        "final": "🥔 <b>Вот картошка на разных языках:</b>\n\n{}"
    }

    async def картошкаcmd(self, message):
        """- показать анимацию с картошкой"""
        await utils.answer(message, self.strings["loading"])
        await sleep(1)

        all_potatoes = [
            "Русский: картошка",
            "Английский: potato",
            "Испанский: patata",
            "Французский: pomme de terre",
            "Немецкий: Kartoffel",
            "Итальянский: patata",
            "Португальский: batata",
            "Украинский: картопля",
            "Белорусский: бульба",
            "Польский: ziemniak",
            "Чешский: brambor",
            "Нидерландский: aardappel",
            "Шведский: potatis",
            "Финский: peruna",
            "Венгерский: burgonya",
            "Турецкий: patates",
            "Арабский: بطاطس (batatis)",
            "Японский: じゃがいも (jagaimo)",
            "Китайский: 土豆 (tǔdòu)",
            "Корейский: 감자 (gamja)"
        ]

        # Первый проход - быстрая анимация
        for i in range(1, 6):
            sample = random.sample(all_potatoes, i)
            await utils.answer(
                message,
                f"🧑‍🌾 <b>Собираю урожай... {i*5}/100%</b>\n\n" + "\n".join(sample)
            )
            await sleep(0.2)

        # Второй проход - полный список
        random.shuffle(all_potatoes)
        for i in range(0, len(all_potatoes), 3):
            await utils.answer(
                message,
                "🌍 <b>Международная картошка:</b>\n\n" + "\n".join(all_potatoes[:i+3])
            )
            await sleep(0.3)

        # Финальный результат (все варианты)
        await utils.answer(
            message,
            self.strings["final"].format("\n".join(all_potatoes))
        )
