# Employee Leave Management System

A full-stack web application for managing employee leave requests and approvals. The system consists of a FastAPI backend and a Streamlit frontend for easy interaction.

## Project Overview

This application provides a complete solution for managing employee leave management with the following features:
- View all employees in the organization
- Submit leave requests with details
- View all submitted leave requests
- Update the status of leave requests (Pending, Approved, Rejected)
- Delete leave requests

## Architecture

The system is built with a **two-tier architecture**:

1. **Backend API** (MAIN.PY) - FastAPI server
2. **Frontend UI** (STREAMLIT.PY) - Streamlit web interface

---

## MAIN.PY - FastAPI Backend

### Overview
`MAIN.PY` is a RESTful API server built with FastAPI that handles all business logic and data management for the leave management system.

### Key Components

#### Default Employees
The system comes with 5 pre-configured employees:
- Rahul (Data Science)
- Priya (Data Analyst)
- Arjun (Machine Learning)
- Sneha (Data Engineering)
- Kiran (Business Intelligence)

#### Data Models

**LeaveRequest Model:**
```python
{
    "employee_id": int,
    "leave_type": str,
    "start_date": str,
    "end_date": str,
    "reason": str
}
```

**StatusUpdate Model:**
```python
{
    "status": str
}
```

#### API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/employees` | Retrieve all employees |
| POST | `/leave-request` | Create a new leave request |
| GET | `/leave-requests` | Retrieve all leave requests |
| PUT | `/leave-request/{request_id}` | Update leave request status |
| DELETE | `/leave-request/{request_id}` | Delete a leave request |

### Features

- **Employee Management**: View all registered employees with their domains
- **Leave Request Creation**: Submit new leave requests with:
  - Employee ID
  - Leave Type (Sick Leave, Casual Leave, Vacation Leave)
  - Start and End Dates
  - Reason for leave
  - Auto-assigned "Pending" status
  
- **Leave Request Management**:
  - View all submitted requests
  - Update request status (Pending → Approved/Rejected)
  - Delete requests
  - Request ID auto-generation

### Technology Stack
- **Framework**: FastAPI
- **Data Validation**: Pydantic
- **Server**: Uvicorn (default)

### Running the Backend
```bash
pip install fastapi uvicorn pydantic
python MAIN.PY
```
The API will be available at `http://127.0.0.1:8000`

---

## STREAMLIT.PY - Frontend UI

### Overview
`STREAMLIT.PY` is an interactive web interface built with Streamlit that provides a user-friendly dashboard for managing leave requests.

### Technology Stack
- **Framework**: Streamlit
- **HTTP Client**: Requests library
- **Data Handling**: Pandas

### Features

#### 1. View Employees
- Displays all employees from the backend
- Shows employee information in a tabular format
- Includes ID, Name, and Domain

#### 2. Create Leave Request
- Form-based interface to submit new leave requests
- Input fields:
  - **Employee ID**: Numeric input (minimum value: 1)
  - **Leave Type**: Dropdown selection
    - Sick Leave
    - Casual Leave
    - Vacation Leave
  - **Start Date**: Text input
  - **End Date**: Text input
  - **Reason**: Text area for detailed explanation
- Success notification upon submission

#### 3. View Leave Requests
- Displays all submitted leave requests in a table format
- Shows:
  - Request ID
  - Employee ID
  - Leave Type
  - Start and End Dates
  - Reason
  - Current Status

#### 4. Update Status
- Allows updating the status of existing leave requests
- Input fields:
  - **Request ID**: Numeric input
  - **Status**: Dropdown with options
    - Pending
    - Approved
    - Rejected
- Confirmation message after update

#### 5. Delete Request
- Remove leave requests from the system
- Input fields:
  - **Request ID**: Numeric input to identify the request
- Confirmation message after deletion

### User Interface

The application uses a sidebar menu for navigation with the following options:
1. View Employees
2. Create Leave Request
3. View Leave Requests
4. Update Status
5. Delete Request

### Configuration

The frontend connects to the backend API at:
```python
BASE_URL = "http://127.0.0.1:8000"
```

### Running the Frontend
```bash
pip install streamlit requests pandas
streamlit run STREAMLIT.PY
```
The web interface will be available at `http://localhost:8501`

---

## Installation & Setup

### Prerequisites
- Python 3.7+
- pip (Python package manager)

### Step 1: Install Dependencies
```bash
pip install fastapi uvicorn pydantic streamlit requests pandas
```

### Step 2: Start the Backend
```bash
python MAIN.PY
```
Expected output: Server running on `http://127.0.0.1:8000`

### Step 3: Start the Frontend (in a new terminal)
```bash
streamlit run STREAMLIT.PY
```
Expected output: Application available at `http://localhost:8501`

---

## Workflow Example

1. **View Employees**: Start by checking available employees
2. **Create Leave Request**: Submit a leave request for an employee
3. **View Leave Requests**: See all submitted requests with status
4. **Update Status**: Approve or reject pending requests
5. **Delete Request**: Remove rejected or cancelled requests

---

## Data Flow

```
User Interface (STREAMLIT.PY)
           ↓
    HTTP Requests (requests library)
           ↓
    FastAPI Backend (MAIN.PY)
           ↓
    In-Memory Data Storage
           ↓
    JSON Response
           ↓
    Display in Streamlit
```

---

## Notes

- **Data Storage**: Currently uses in-memory lists. Data will be lost on server restart.
- **Database Integration**: For production, consider integrating a database (PostgreSQL, MongoDB, etc.)
- **Validation**: Date format should be consistently handled (recommend ISO 8601 format: YYYY-MM-DD)
- **Error Handling**: Current implementation provides basic error messages. Enhanced error handling can be added for production.

---

## Future Enhancements

- Database integration for persistent storage
- User authentication and authorization
- Email notifications for leave approvals
- Leave balance tracking
- Advanced filtering and search
- Leave type policies and limits
- Manager approval workflow
- Reporting and analytics

---

## Author

vasanth373

## License

This project is open source and available under the MIT License.
