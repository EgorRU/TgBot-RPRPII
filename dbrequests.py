from models import async_session
from models import User
from sqlalchemy import select, update
import datetime


def connection(func):
    async def wrapper(*args, **kwargs):
        async with async_session() as session:
            return await func(session, *args, **kwargs)

    return wrapper


@connection
async def update_db(session, message):
    tg_id = message.from_user.id
    fullname = message.from_user.full_name
    username = message.from_user.username
    time_last = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    action_last = message.text if getattr(
        message, 'text', None) else message.data if getattr(message, 'data', None) else None

    user = await session.scalar(select(User).where(User.tg_id == tg_id))
    if not user:
        session.add(
            User(
                tg_id=tg_id,
                fullname=fullname,
                username=username,
                time_register=time_last,
                time_last=time_last,
                action_last=action_last,
                count=1,
            )
        )
    else:
        await session.execute(
            update(User)
            .where(User.tg_id == tg_id)
            .values(
                fullname=fullname,
                username=username,
                time_last=time_last,
                action_last=action_last,
                count=User.count + 1,
            )
        )
    await session.commit()
