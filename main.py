from fastapi import FastAPI
from app.api import router as api_router
import os
import dotenv
dotenv.load_dotenv()
app = FastAPI()

app.include_router(api_router)

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run("main:app", host=os.environ.get("HOST", "0.0.0.0"), port=int(os.environ.get("PORT")))
