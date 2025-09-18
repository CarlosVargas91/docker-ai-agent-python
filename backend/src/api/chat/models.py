from datetime import datetime, timezone
from email import message
from email.policy import default
import time
from sqlmodel import SQLModel, Field, DateTime

def get_utc_now():
    return datetime.now().replace(tzinfo=timezone.utc)

class ChatMessagePayload(SQLModel):
    # validation
    # serializer
    message: str

class ChatMessage(SQLModel, table=True):
    # database table
    # saving, updating, getting, deleting
    # serializer
    id: int | None = Field(default=None, primary_key=True) # Increments automatic like 1->2->3
    message: str
    created_at: datetime = Field(
        default_factory = get_utc_now,
        sa_type=DateTime(timezone=True),
        primary_key=False,
        nullable=False,
    )

class ChatMessageListItem(SQLModel):
    id: int | None = Field(default=None)
    message: str
    created_at: datetime = Field(default=None)