import uvicorn
from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import RedirectResponse

app = FastAPI(debug=True)


@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse("/docs")

@app.get("/distance_change/", description="Перетворення відстані у футах на ярди, милі та дюйми.")
def calkulator(num1: float = Query(..., description="Уведіть значення відстані у Футах для конвертації ."),
               operation: str = Query(..., description="Оберіть значення в яке хочете конвертувати відстань: Yards, Miles, Inches.")):
    try:
        if operation == "Ярди" or operation == "Yards":
            result = num1 * 0.333333333

        elif operation == "Милі" or operation == "Miles":
            result = num1 * 0.000189393939

        elif operation == "Дюйми" or operation == "Inches":
            result = num1 * 12

        else:
            raise HTTPException(status_code=400,
                                detail="Операція є невірною. Спробуйте: Yards/Ярди, або Miles/Милі, або Inches/Дюйми.")

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    return {"result": result}




if __name__ == "__main__":
    uvicorn.run("main:app", reload = True)