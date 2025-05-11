from .. import loader, utils
from asyncio import sleep
import random

@loader.tds
class PotatoAnimMod(loader.Module):
    """������������� �������� �� ���� ������"""
    strings = {
        "name": "@YMEPOTBAC �������� �� ���� ������",
        "loading": "<i>�������� ������������ ��������...</i>",
        "final": "?? <b>�������� �� ������ ������:</b>\n\n{}"
    }

    async def potatocmd(self, message):
        """- ������������� ����� �������� �� ������ ������"""
        await utils.answer(message, self.strings["loading"])
        await sleep(1)

        potatoes = [
            "�������: ��������",
            "����������: potato",
            "���������: patata",
            "�����������: pomme de terre",
            "��������: Kartoffel",
            "�����������: patata",
            "�������������: batata",
            "����������: ��������",
            "�����������: ������",
            "��������: ziemniak",
            "�������: brambor",
            "�������������: aardappel",
            "��������: potatis",
            "�������: peruna",
            "����������: burgonya",
            "��������: patates",
            "��������: ????? (batatis)",
            "��������: ????? (jagaimo)",
            "���������: ?? (tudou)",
            "���������: ?? (gamja)"
        ]

        # ������������ ������
        random.shuffle(potatoes)
        
        # ������� 2 ����� ��������
        for cycle in range(2):
            # ���������� ������ ������� �� �������
            for i in range(len(potatoes)):
                current = "\n".join(potatoes[:i+1])
                await utils.answer(
                    message, 
                    f"?? <b>������� ��������... (���� {cycle+1}/2)</b>\n\n{current}"
                )
                await sleep(0.3)  # �������� ����� ����������� ������

        # ��������� ��������� (15 ��������� ���������)
        selected = random.sample(potatoes, min(15, len(potatoes)))
        await utils.answer(
            message, 
            self.strings["final"].format("\n".join(selected))