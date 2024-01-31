from src.services import  fetch_data_from_table,add_student,update_student_status,datetime,delete_student_data,parse_date,app,connect_to_database


@app.get("/")
def read_root():
    conn = connect_to_database()
    rows = fetch_data_from_table(conn)
    return {"data": rows}


@app.get("/getStudents/")
def get_students(id: int = None):
    conn = connect_to_database()
    data = fetch_data_from_table(conn, id)
    return {"data": data}


@app.post("/addStudent")
def add_student_route(name: str, dob: str, status: str):
    conn = connect_to_database()
    message = add_student(conn, name, dob, status)
    conn.close()
    return message

@app.put("/update/{student_id}")
def update_status(student_id: int, status: str):
    conn = connect_to_database()
    data = update_student_status(conn, student_id, status)
    conn.close()
    return {"data": data}


@app.delete("/delete/{student_id}")
def delete_student(student_id: int):
    conn = connect_to_database()
    data = delete_student_data(conn, student_id)
    conn.close()
    return {"data": data}