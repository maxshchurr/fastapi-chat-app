import uuid
from uuid import UUID
from pydantic import BaseModel
from app.users_countries_data.extract_countries import COUNTRIES


class ChatUser(BaseModel):
    id: str | None = str(uuid.uuid4())
    username: str
    country: str
    chats: list | None = []

    # @property
    def check_if_country_is_valid(self):
        return self.country in COUNTRIES


class LoginUser(BaseModel):
    username: str
    country: str


class Chat(BaseModel):
    id: UUID
    topic: str
    members: list


class ChatTopics(BaseModel):
    id: int
    topic: str
