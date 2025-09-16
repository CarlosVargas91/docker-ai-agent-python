from sqlmodel import SQLModel, Field

class ChatMessagePayload(SQLModel):
    # validation
    message: str

class ChatMessage(SQLModel, table=True):
    # database table
    # saving, updating, getting, deleting
    id: int | None = Field(default=None, primary_key=True) # Increments automatic like 1->2->3
    message: str