import uvicorn
from fastapi import FastAPI
from src.webinar.routes import router as router_webinar
from src.course.routes import router as router_course
app = FastAPI(title="Вебинар")

app.include_router(router_webinar)
app.include_router(router_course)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=5000)
# uvicorn --host localhost --port 5000 src.main:app --reload

