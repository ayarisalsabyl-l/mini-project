from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Student Performance API",
    version="1.0.0"
)

class StudentInput(BaseModel):
    study_hours: float
    attendance: float
    previous_score: float
    assignments_completed: int

@app.get("/")
def home():
    return {"message": "Student Performance API is running"}
@app.post("/predict")
def predict(student: StudentInput):
    score = (student.study_hours * 5
        + student.attendance * 0.2
        + student.previous_score * 0.3
        + student.assignments_completed)
    result = "Pass" if score >= 50 else "Fail"
    return {"predicted_score": round(score, 2), "result": result}