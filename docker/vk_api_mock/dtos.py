from pydantic import BaseModel


class UsernameResponse(BaseModel):
    vk_id: str | None
