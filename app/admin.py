from aiogram import Router, F
from config import ADMIN
from aiogram.types import Message


router_admin = Router()


@router_admin.message(F.document, F.from_user.id == ADMIN)
async def get_document(message: Message):
    await message.answer(message.document.file_id)
