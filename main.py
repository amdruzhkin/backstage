from fastapi import FastAPI
import uvicorn
import authentication

app = FastAPI()
app.include_router(authentication.router)


# if __name__ == '__main__':
#     uvicorn.run(app='main:app', host="0.0.0.0", port=8000, reload=True)