# Python Learning API

This API is designed to manage student records stored in a MySQL database. It provides endpoints for retrieving, updating, adding, and deleting student data. The API is built using FastAPI, a modern web framework for building APIs with Python.

## Features

- **Retrieve Students**: Get a list of all students or retrieve a specific student by their ID.
- **Update Student Status**: Update the status of a student (Active or Inactive) by their ID.
- **Add New Student**: Add a new student to the database.
- **Delete Student**: Delete a student from the database by their ID.

## Installation

1. Clone the repository to your local machine:

```
git clone https://github.com/your-username/python-learning-api.git
```

2. Navigate to the project directory:

```
cd python-learning-api
```

3. Install dependencies:

```
pip install -r requirements.txt
```

4. Configure the MySQL database connection by modifying the `connect_to_database` function in `main.py`.

5. Run the FastAPI application:

```
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`.

## Usage

- Use HTTP GET requests to retrieve student data.
- Use HTTP PUT requests to update student status.
- Use HTTP POST requests to add new students.
- Use HTTP DELETE requests to delete students.

Refer to the API documentation or OpenAPI (Swagger) UI for detailed usage instructions.

## API Documentation

The API documentation is available at `http://localhost:8000/docs` when the application is running.

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvement, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
