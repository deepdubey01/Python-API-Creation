from fastapi import FastAPI, HTTPException, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from src.services import (
    fetch_data_from_table,
    add_student,
    update_student_status,
    delete_student_data,
    add_teacher,
    update_teacher_status,
    delete_teacher_data,
)
from datetime import datetime

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

student_router = APIRouter(prefix="/student", tags=["Student"])
teacher_router = APIRouter(prefix="/teacher", tags=["Teacher"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the API!"}

@student_router.get("/")
def get_students(id: int = None):
    data = fetch_data_from_table(id,'students')
    return {"data": data}

@student_router.post("/")
def add_student_route(name: str, dob: str, status: str):
    message = add_student(name, dob, status)
    return message

@student_router.put("/{student_id}")
def update_student(student_id: int, status: str):
    data = update_student_status(student_id, status)
    return {"data": data}

@student_router.delete("/{student_id}")
def delete_student(student_id: int):
    data = delete_student_data(student_id)
    return {"data": data}

@teacher_router.get("/")
def get_teachers(id: int = None):
    data = fetch_data_from_table(id,'teachers')
    return {"data": data}

@teacher_router.post("/")
def add_teacher_route(name: str, dob: str, status: str):
    message = add_teacher(name, dob, status)
    return message

@teacher_router.put("/{teacher_id}")
def update_teacher(teacher_id: int, status: str):
    data = update_teacher_status(teacher_id, status)
    return {"data": data}

@teacher_router.delete("/{teacher_id}")
def delete_teacher(teacher_id: int):
    data = delete_teacher_data(teacher_id)
    return {"data": data}

app.include_router(student_router)
app.include_router(teacher_router)
