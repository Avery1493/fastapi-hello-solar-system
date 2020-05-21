# python main.py

# Import 
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import pandas as pd
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

# Instantiate App
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


#ROUTES
# Hello Page
@app.get("/hello")
async def hello():
    """
    Displays the message Hello, Solar System!
    """
    return {"message": "Hello, Solar System!"}


# Fake News Page
@app.get("/")
async def root():
    """
    Fake News Detector API  
    Verifies the API is deployed, and links to the docs
    """
    return HTMLResponse("""
    <h1>Fake News Detector API</h1>
    <p>Go to <a href="/docs">/docs</a> for documentation.</p>
    <p>Go to <a href="/hello">/hello</a> for hello.</p>
    <p>Go to <a href="/predict">/predict</a> for prediction.</p>
    """)

# Class for Inputs
class Story(BaseModel):
  title: str
  text : str


# Prediction Page
@app.post('/predict')
async def predict(story: Story):
    """
    Predicts whether a news article is real or fake news, 
    based on its title

    Naive baseline: Always predicts 'fake'
    """

    # Doesn't do anything with the request body yet,
    # just verifies we can read it.
    print(story)
    X = pd.DataFrame([dict(story)])
    print(X.to_markdown())

    return {
        'prediction': 'fake', 
        'probability': 0.50
    }