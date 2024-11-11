#bot api key - 03d2ace33d7ac0e1ca19234a67923d6bf6744f5826fa7b21c02f1568271819cc
#room id - 670a5014b051ea906be70c51

from highrise import BaseBot
from highrise.models import SessionMetadata
from highrise import *
from highrise.models import *


class Swini(BaseBot):

    async def on_start(self, session_metadata: SessionMetadata) -> None:
        await self.highrise.chat("Welcome")

    async def on_user_join(self, user: User,
                           position: Position | AnchorPosition) -> None:
        await self.highrise.chat(f"Welcome {user.username}!")

    async def on_chat(self, user: User, message: str) -> None:
        if message.startswith("1"):
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-tiktok2", roomUser.id)
