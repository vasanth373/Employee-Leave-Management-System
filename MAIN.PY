from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Default Employees
employees = [
    {"id": 1, "name": "Rahul", "domain": "Data Science"},
    {"id": 2, "name": "Priya", "domain": "Data Analyst"},
    {"id": 3, "name": "Arjun", "domain": "Machine Learning"},
    {"id": 4, "name": "Sneha", "domain": "Data Engineering"},
    {"id": 5, "name": "Kiran", "domain": "Business Intelligence"}
]

leave_requests = []


class LeaveRequest(BaseModel):
    employee_id: int
    leave_type: str
    start_date: str
    end_date: str
    reason: str


class StatusUpdate(BaseModel):
    status: str


# Read Employees
@app.get("/employees")
def get_employees():
    return employees


# Create Leave Request
@app.post("/leave-request")
def create_leave(request: LeaveRequest):

    request_id = len(leave_requests) + 1

    leave = {
        "request_id": request_id,
        "employee_id": request.employee_id,
        "leave_type": request.leave_type,
        "start_date": request.start_date,
        "end_date": request.end_date,
        "reason": request.reason,
        "status": "Pending"
    }

    leave_requests.append(leave)

    return {
        "message": "Leave Request Created",
        "data": leave
    }


# Read Leave Requests
@app.get("/leave-requests")
def get_leave_requests():
    return leave_requests


# Update Status
@app.put("/leave-request/{request_id}")
def update_status(request_id: int, update: StatusUpdate):

    for leave in leave_requests:

        if leave["request_id"] == request_id:

            leave["status"] = update.status

            return {
                "message": "Status Updated",
                "data": leave
            }

    return {"message": "Request Not Found"}


# Delete Request
@app.delete("/leave-request/{request_id}")
def delete_request(request_id: int):

    for leave in leave_requests:

        if leave["request_id"] == request_id:

            leave_requests.remove(leave)

            return {
                "message": "Request Deleted"
            }

    return {"message": "Request Not Found"}