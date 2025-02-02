from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Enable CORS for cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load student marks data from JSON file
with open("marks.json", "r") as file:
    marks_data = json.load(file)

@app.get("/api")
def get_marks(name: list[str]):
    """Returns marks of the given names."""
    response = {"marks": [marks_data.get(n, "Not Found") for n in name]}
    return response
