from fastapi import FastAPI
import uvicorn
import sys
import os
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from text_summarization.pipeline.prediction import PredictionPipeline


text:str = "What is Text Summarization ?"

app = FastAPI()

@app.get("/", tags = ["authentication"])
async def index():
    return RedirectResponse(url="/docs")

@app.post("/predict")
async def predict_route(text):
    try:
        obj = PredictionPipeline()
        text = obj.predict(text)
        return {"Summary": text}
    except Exception as e:
        raise e
    

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)