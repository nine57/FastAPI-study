import asyncio
import time

import aiohttp
from config import API_KEY, TARGET_URL
from sqlalchemy.orm import Session

from . import models


async def get_school_data(db: Session):
    return db.query(models.SchoolCode).all()


async def set_params(regulator, code):
    params = {
        "KEY": API_KEY,
        "Type": "json",
        "pIndex": 1,
        "pSize": 1000,
        "AY": 2022,
        "SEM": 2,
        "TI_FROM_YMD": 20221003,
        "TI_TO_YMD": 20221007,
        "ATPT_OFCDC_SC_CODE": regulator,
        "SD_SCHUL_CODE": code,
    }
    return params


async def request_to_target(idx, school):
    regulator = school.regulator
    code = school.code
    params = await set_params(regulator=regulator, code=code)
    async with aiohttp.ClientSession() as session:
        async with session.get(TARGET_URL, params=params) as response:
            data = await response.json(content_type=None)
            try:
                school_name = data["hisTimetable"][1]["row"][0]["SCHUL_NM"]
            except KeyError:
                school_name = "Key Error"
            print(idx, school_name)


async def get_data(db):
    schools = await get_school_data(db=db)
    start = time.time()
    cycle = len(schools) // 100
    for i in range(cycle):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(
            asyncio.gather(
                *(
                    request_to_target(idx=100 * i + idx, school=school)
                    for idx, school in enumerate(schools[100 * i : 100 * (i + 1)])
                )
            )
        )
    end = time.time()
    execute_time = f"{round(end-start,2)}s"
    print(execute_time)
