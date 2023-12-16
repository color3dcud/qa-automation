from fastapi import FastAPI, HTTPException
from faker import Faker

from dtos import UsernameResponse

app = FastAPI()
fake = Faker()


@app.get(
    path='/vk_id/{username}',
    description='Получение VK ID',
    response_model=UsernameResponse
)
async def vk_id(username):

    if username == 'test_mock':
        return UsernameResponse(vk_id=username)

    elif username.lower() != 'not_found':
        profile = fake.profile()
        vk_id_value = f"{username}_{profile['username']}"
        return UsernameResponse(vk_id=vk_id_value)

    else:
        raise HTTPException(status_code=404)
