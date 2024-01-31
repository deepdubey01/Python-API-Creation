from datetime import datetime
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from src.services import fetch_data_from_table, add_student, update_student_status, delete_student_data

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/student/")
def get_students(id: int = None):
    data = fetch_data_from_table(id)
    return {"data": data}

@app.post("/student/")
def add_student_route(name: str, dob: str, status: str):
    message = add_student(name, dob, status)
    return message

@app.put("/student/{student_id}")
def update_status(student_id: int, status: str):
    data = update_student_status(student_id, status)
    return {"data": data}

@app.delete("/student/{student_id}")
def delete_student(student_id: int):
    data = delete_student_data(student_id)
    return {"data": data}
