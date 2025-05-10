# meta developer: @YMEPOTBAC

import asyncio
from .. import loader, utils
from telethon.errors import MessageNotModifiedError

@loader.tds
class RomanticMessagesMod(loader.Module):
    """������������� ��������� � 1001 ����� � �����������"""

    strings = {
        "name": "@YMEPOTBAC ��������� � �������",
        "not_subscribed": "<b>��� ������������� ���� ������� ���������� ����������� �� �����</b>",
    }

    def __init__(self):
        self.name = self.strings["name"]
        self._me = None

    async def client_ready(self, client, db):
        self.client = client
        self.db = db
        self.is_ready = True

    @loader.command(ru_doc="�������� 1001 ����")
    async def surprise(self, message):
        """��������� 1001 ����"""
        try:
            is_subscribed = True  # ����� �������� �������� ��������

            if not is_subscribed:
                await utils.answer(message, self.strings["not_subscribed"])
                return

            # ���������� ��������� � ������
            await utils.answer(message, "������� 1001 ���� ��� ���... ??")

            # ���������� ���� �������� �� 100 ����
            roses = []
            for i in range(1, 1002):
                roses.append("??")
                if i % 100 == 0 or i == 1001:
                    await message.respond("".join(roses))
                    roses = []
                    await asyncio.sleep(0.5)

            # ��������� ���������
            await message.respond("?? 1001 ���� ��� ����! ??")

        except Exception as e:
            print(f"������ � ������� surprise: {e}")

    @loader.command(ru_doc="1001 ���������")
    async def sorry(self, message):
        """��������� 1001 ���������"""
        try:
            is_subscribed = True  # ����� �������� �������� ��������

            if not is_subscribed:
                await utils.answer(message, self.strings["not_subscribed"])
                return

            # ���������� ��������� � ������
            msg = await utils.answer(message, "������� 1001 ���������...")

            # ���������� ��������� �������� �� 10 ����
            apologies = []
            for i in range(1, 1002):
                apology = f"������ ����, � ��������� {i}/1001"
                apologies.append(apology)
                
                if i % 10 == 0 or i == 1001:
                    try:
                        await msg.edit("\n".join(apologies))
                    except MessageNotModifiedError:
                        pass
                    
                    if i != 1001:
                        await asyncio.sleep(1)
                    
                    if i % 100 == 0:
                        apologies = []  # ������� ������ ����� �� ����������� ���������

            # ��������� ���������
            await message.respond("� �������� �������! ??")

        except Exception as e:
            print(f"������ � ������� sorry: {e}")