from aiogram import Bot, Dispatcher
from app.admin import router_admin
from app.client import router_client
from app.module_1 import router_module_1
from app.module_2 import router_module_2
from app.module_3 import router_module_3
from app.module_4 import router_module_4
from app.module_5 import router_module_5
from app.module_6 import router_module_6
from app.module_7 import router_module_7
from app.module_8 import router_module_8
from config import TOKEN_WORK_BOT
import asyncio


bot = Bot(token=TOKEN_WORK_BOT)
dp = Dispatcher()


async def main():
    dp.include_router(router_client)
    dp.include_router(router_module_1)
    dp.include_router(router_module_2)
    dp.include_router(router_module_3)
    dp.include_router(router_module_4)
    dp.include_router(router_module_5)
    dp.include_router(router_module_6)
    dp.include_router(router_module_7)
    dp.include_router(router_module_8)
    dp.include_router(router_admin)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())