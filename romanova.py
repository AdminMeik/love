# meta developer: @YMEPOTBAC

import asyncio
from .. import loader, utils
from telethon.errors import MessageNotModifiedError

@loader.tds
class RomanovaMod(loader.Module):
    """������ � �������� ��������� ������ ��� ���� ��������"""

    strings = {
        "name": "@YMEPOTBAC ��������",
        "not_subscribed": "<b>��� ������������� ���� ������� ���������� ����������� �� �����</b>",
    }

    def __init__(self):
        self.name = self.strings["name"]
        self._me = None
        self.text_frames = [
            "�",
            "��",
            "���",
            "����",
            "���� ",
            "���� �",
            "���� ��",
            "���� ���",
            "���� ����",
            "���� �����",
            "���� ��������",
            "���� �������� ",
            "���� �������� �",
            "���� �������� ��",
            "���� �������� ���",
            "���� �������� ����",
            "���� �������� ���� ",
            "���� �������� ���� �",
            "���� �������� ���� ��",
            "���� �������� ���� ���",
            "���� �������� ���� ����",
            "���� �������� ���� �����",
            "���� �������� ���� ������",
            "���� �������� ���� ������ ",
            "���� �������� ���� ������ �",
            "���� �������� ���� ������ ��",
            "���� �������� ���� ������ ���",
            "���� �������� ���� ������ ����",
            "���� �������� ���� ������ �����",
            "���� �������� ���� ������ ������",
            "���� �������� ���� ������ �������",
            "���� �������� ���� ������ ��������",
            "���� �������� ���� ������ ��������!",
            "���� �������� ���� ������ ��������!!",
            "���� �������� ���� ������ ��������!!!",
        ]

    async def client_ready(self, client, db):
        self.client = client
        self.db = db
        self.is_ready = True

    @loader.command(ru_doc="������ ��������� ������ ��� ���� ��������")
    async def romanova(self, message):
        """������ ��������� ������"""
        try:
            is_subscribed = True  # ����� �������� �������� ��������

            if not is_subscribed:
                await utils.answer(message, self.strings["not_subscribed"])
                return

            for frame in self.text_frames:
                try:
                    await utils.answer(message, frame)
                    await asyncio.sleep(0.15)  # ������� ������
                except MessageNotModifiedError:
                    pass
            
            # ��������� ������� � �����
            for _ in range(3):
                try:
                    await utils.answer(message, "���� �������� ���� ������ ��������!!!")
                    await asyncio.sleep(0.5)
                    await utils.answer(message, "���� �������� ���� ������ ��������   ")
                    await asyncio.sleep(0.2)
                except MessageNotModifiedError:
                    pass

        except Exception as e:
            print(f"������ � ��������: {e}")