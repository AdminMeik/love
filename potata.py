from .. import loader, utils
from asyncio import sleep
import random

@loader.tds
class PotatoAnimMod(loader.Module):
    """Анимированная картошка на всех языках"""
    strings = {
        "name": "@YMEPOTBAC картошка на всех языках",
        "loading": "<i>Загружаю картофельные переводы...</i>",
        "final": "?? <b>Картошка на разных языках:</b>\n\n{}"
    }

    async def potatocmd(self, message):
        """- анимированный показ картошки на разных языках"""
        await utils.answer(message, self.strings["loading"])
        await sleep(1)

        potatoes = [
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
            "Арабский: ????? (batatis)",
            "Японский: ????? (jagaimo)",
            "Китайский: ?? (tudou)",
            "Корейский: ?? (gamja)"
        ]

        # Перемешиваем список
        random.shuffle(potatoes)
        
        # Создаем 2 цикла анимации
        for cycle in range(2):
            # Показываем каждый вариант по очереди
            for i in range(len(potatoes)):
                current = "\n".join(potatoes[:i+1])
                await utils.answer(
                    message, 
                    f"?? <b>Собираю картошку... (цикл {cycle+1}/2)</b>\n\n{current}"
                )
                await sleep(0.3)  # Задержка между добавлением языков

        # Финальный результат (15 случайных вариантов)
        selected = random.sample(potatoes, min(15, len(potatoes)))
        await utils.answer(
            message, 
            self.strings["final"].format("\n".join(selected))