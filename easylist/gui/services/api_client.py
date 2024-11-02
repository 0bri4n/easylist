import aiohttp
from gui.consts import BASE_URL

from easylist.api.application.dtos.student_dto import StudentCreateDTO

CREATED_STATUS_CODE = 201


async def create_student(student_data: StudentCreateDTO) -> dict:
    url = f"{BASE_URL}/students"
    async with aiohttp.ClientSession() as session, session.post(url, json=student_data.model_dump()) as response:
        if response.status == CREATED_STATUS_CODE:
            return await response.json()
        raise RuntimeError(await response.text())
