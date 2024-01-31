from datetime import datetime
from http.client import HTTPException
from mysql.connector import Error
from dbConnection.database import DatabaseConnection

db_instance = DatabaseConnection()


def fetch_data_from_table(id=None, table_name=str):
    conn = db_instance.get_connection()
    cursor = None
    try:
        cursor = conn.cursor()
        if id is None:
            query = f"SELECT * FROM {table_name}"
            cursor.execute(query)
        else:
            query = f"SELECT * FROM {table_name} WHERE id = %s"
            cursor.execute(query, (id,))
        rows = cursor.fetchall()
        columns = [col[0] for col in cursor.description]
        result = []
        for row in rows:
            row_data = {}
            for i in range(len(columns)):
                row_data[columns[i]] = row[i]
            result.append(row_data)
        return result
    except Error as e:
        print("Error:", e)
        raise
    finally:
        if cursor:
            cursor.close()


def update_student_status(student_id: int, status: str):
    conn = db_instance.get_connection()
    cursor = None
    try:
        cursor = conn.cursor()
        if status in ['Active', 'Inactive']:
            query = "UPDATE students SET status = %s WHERE id = %s"
            cursor.execute(query, (status, student_id))
            conn.commit()
            return {"message": f"Status updated to {status} successfully"}
        else:
            raise HTTPException(status_code=400, detail="Invalid status")
    except Error as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if cursor:
            cursor.close()

def delete_student_data(student_id: int):
    conn = db_instance.get_connection()
    cursor = None
    try:
        cursor = conn.cursor()
        query = "DELETE FROM students WHERE id = %s"
        cursor.execute(query, (student_id,))
        conn.commit()
        return {"message": f"Student with ID {student_id} deleted successfully"}
    except Error as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if cursor:
            cursor.close()

def add_student(name: str, dob: str, status: str):
    conn = db_instance.get_connection()
    cursor = None
    try:
        dob_formatted = parse_date(dob)
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM students WHERE name = %s AND dob = %s", (name, dob_formatted))
        existing_student = cursor.fetchone()
        
        if existing_student:
            raise HTTPException(status_code=400, detail="Student with the same data already exists")
        cursor.execute("SELECT rollno FROM students ORDER BY rollno DESC LIMIT 1")
        last_roll = cursor.fetchone()
        
        if last_roll:
            last_roll_number = last_roll[0]
            next_roll_number = int(last_roll_number[1:]) + 1
            new_rollno = f"S{next_roll_number:03}" 
        else:
            new_rollno = "S001"
    
        query = "INSERT INTO students (name, rollno, dob, status) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (name, new_rollno, dob_formatted, status))
        conn.commit()
        return {"message": "Student added successfully"}
    except Error as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if cursor:
            cursor.close()

def parse_date(dob):
    date_formats = ['%d/%m/%Y', '%Y/%m/%d', '%m-%Y-%d', '%Y-%m-%d']
    for fmt in date_formats:
        try:
            dob_date = datetime.strptime(dob, fmt)
            return dob_date.strftime('%Y-%m-%d')
        except ValueError:
            pass
    raise ValueError("Invalid date format")





def update_teacher_status(student_id: int, status: str):
    conn = db_instance.get_connection()
    cursor = None
    try:
        cursor = conn.cursor()
        if status in ['Active', 'Inactive']:
            query = "UPDATE teachers SET status = %s WHERE id = %s"
            cursor.execute(query, (status, student_id))
            conn.commit()
            return {"message": f"Status updated to {status} successfully"}
        else:
            raise HTTPException(status_code=400, detail="Invalid status")
    except Error as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if cursor:
            cursor.close()

def delete_teacher_data(student_id: int):
    conn = db_instance.get_connection()
    cursor = None
    try:
        cursor = conn.cursor()
        query = "DELETE FROM teachers WHERE id = %s"
        cursor.execute(query, (student_id,))
        conn.commit()
        return {"message": f"Student with ID {student_id} deleted successfully"}
    except Error as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if cursor:
            cursor.close()

def add_teacher(name: str, dob: str, status: str):
    conn = db_instance.get_connection()
    cursor = None
    try:
        dob_formatted = parse_date(dob)
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM teachers WHERE name = %s AND dob = %s", (name, dob_formatted))
        existing_student = cursor.fetchone()
        
        if existing_student:
            raise HTTPException(status_code=400, detail="Student with the same data already exists")
        cursor.execute("SELECT rollno FROM students ORDER BY rollno DESC LIMIT 1")
        last_roll = cursor.fetchone()
        
        if last_roll:
            last_roll_number = last_roll[0]
            next_roll_number = int(last_roll_number[1:]) + 1
            new_rollno = f"S{next_roll_number:03}" 
        else:
            new_rollno = "S001"
    
        query = "INSERT INTO students (name, rollno, dob, status) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (name, new_rollno, dob_formatted, status))
        conn.commit()
        return {"message": "Student added successfully"}
    except Error as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if cursor:
            cursor.close()

# def fetch_teachers_from_table(id=None):
    conn = db_instance.get_connection()
    cursor = None
    try:
        cursor = conn.cursor()
        if id is None:
            query = "SELECT * FROM students"
            cursor.execute(query)
        else:
            query = "SELECT * FROM students WHERE id = %s"
            cursor.execute(query, (id,))
        rows = cursor.fetchall()
        columns = [col[0] for col in cursor.description]
        result = []
        for row in rows:
            row_data = {}
            for i in range(len(columns)):
                row_data[columns[i]] = row[i]
            result.append(row_data)
        return result
    except Error as e:
        print("Error:", e)
        raise 
    finally:
        if cursor:
            cursor.close()