from fastapi import FastAPI

from routers import budget

app = FastAPI()

app.include_router(budget.router)
