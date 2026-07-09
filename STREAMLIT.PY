import streamlit as st
import requests
import pandas as pd

BASE_URL = "http://127.0.0.1:8000"

st.title("Employee Leave Management System")

menu = st.sidebar.selectbox(
    "Select Option",
    [
        "View Employees",
        "Create Leave Request",
        "View Leave Requests",
        "Update Status",
        "Delete Request"
    ]
)

# View Employees
if menu == "View Employees":

    response = requests.get(
        f"{BASE_URL}/employees"
    )

    employees = response.json()

    st.subheader("Employee List")

    st.dataframe(
        pd.DataFrame(employees)
    )

# Create Leave Request
elif menu == "Create Leave Request":

    st.subheader("Apply Leave")

    employee_id = st.number_input(
        "Employee ID",
        min_value=1
    )

    leave_type = st.selectbox(
        "Leave Type",
        [
            "Sick Leave",
            "Casual Leave",
            "Vacation Leave"
        ]
    )

    start_date = st.text_input(
        "Start Date"
    )

    end_date = st.text_input(
        "End Date"
    )

    reason = st.text_area(
        "Reason"
    )

    if st.button("Submit"):

        payload = {
            "employee_id": employee_id,
            "leave_type": leave_type,
            "start_date": start_date,
            "end_date": end_date,
            "reason": reason
        }

        requests.post(
            f"{BASE_URL}/leave-request",
            json=payload
        )

        st.success(
            "Leave Request Submitted"
        )

# View Leave Requests
elif menu == "View Leave Requests":

    response = requests.get(
        f"{BASE_URL}/leave-requests"
    )

    requests_data = response.json()

    st.subheader("Leave Requests")

    st.dataframe(
        pd.DataFrame(requests_data)
    )

# Update Status
elif menu == "Update Status":

    request_id = st.number_input(
        "Request ID",
        min_value=1
    )

    status = st.selectbox(
        "Status",
        [
            "Pending",
            "Approved",
            "Rejected"
        ]
    )

    if st.button("Update"):

        requests.put(
            f"{BASE_URL}/leave-request/{request_id}",
            json={"status": status}
        )

        st.success(
            "Status Updated"
        )

# Delete Request
elif menu == "Delete Request":

    request_id = st.number_input(
        "Request ID",
        min_value=1
    )

    if st.button("Delete"):

        requests.delete(
            f"{BASE_URL}/leave-request/{request_id}"
        )

        st.success(
            "Request Deleted"
        )