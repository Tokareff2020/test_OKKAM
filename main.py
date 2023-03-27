from fastapi import FastAPI

from db.db_controller import get_respondent_from_str


app = FastAPI()


@app.get("/")
async def index():
    return {'message': 'privet'}


@app.get("/getPercent")
async def get_percent(audience1: str = '', audience2: str = ''):
    """Получить процент вхождения второй аудитории в первую, основываясь на среднем Weight"""
    audience1 = await get_respondent_from_str(audience1)
    audience2 = await get_respondent_from_str(audience2)
    audience1_weight = set(map(lambda x: x[1], audience1))
    audience2_weight = set(map(lambda x: x[1], audience2))

    if audience1_weight:
        percentage = sum(audience1_weight & audience2_weight) / sum(audience1_weight)
    else:
        percentage = 0

    return {"percent": percentage * 100}


