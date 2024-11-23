import sqlite3
import datetime


async def update_BD(message, command):
    current_time = str(datetime.datetime.now())[:19]
    base = sqlite3.connect("database.db")
    cur = base.cursor()
    base.execute(
        "CREATE TABLE IF NOT EXISTS registration_data(id PRIMARY KEY, fullname TEXT, username TEXT, time_register TEXT, last_time TEXT, last_action TEXT, count INTEGER, active TEXT)"
    )
    base.commit()
    id = cur.execute(
        f"SELECT id FROM registration_data WHERE id={message.from_user.id}"
    ).fetchone()
    if id is None:
        cur.execute(
            "INSERT INTO registration_data values(?,?,?,?,?,?,?,?)",
            (
                message.from_user.id,
                message.from_user.full_name,
                message.from_user.username,
                current_time,
                current_time,
                command,
                1,
                "1",
            ),
        )
        base.commit()
    else:
        cur.execute(
            "UPDATE registration_data SET fullname==?, username==?, last_time==?, last_action==? WHERE id=?",
            (
                message.from_user.full_name,
                message.from_user.username,
                current_time,
                command,
                message.from_user.id,
            ),
        )
        base.commit()
        count = int(
            cur.execute(
                f"SELECT count FROM registration_data WHERE id={message.from_user.id}"
            ).fetchone()[0]
        )
        cur.execute(
            "UPDATE registration_data SET count==? WHERE id=?",
            (count + 1, message.from_user.id),
        )
        base.commit()
    base.close()
