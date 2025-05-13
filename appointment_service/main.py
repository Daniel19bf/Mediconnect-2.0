
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uuid

app = FastAPI()

appointments_db = []

class Appointment(BaseModel):
    id: Optional[str]
    patient_id: str
    doctor_id: str
    date: str
    time: str

@app.post("/appointments")
def create_appointment(appointment: Appointment):
    appointment.id = str(uuid.uuid4())
    appointments_db.append(appointment)
    return {"message": "Appointment created", "appointment_id": appointment.id}

@app.get("/appointments/user/{user_id}")
def get_appointments(user_id: str):
    result = [appt for appt in appointments_db if appt.patient_id == user_id or appt.doctor_id == user_id]
    return result

@app.delete("/appointments/{appointment_id}")
def delete_appointment(appointment_id: str):
    global appointments_db
    appointments_db = [appt for appt in appointments_db if appt.id != appointment_id]
    return {"message": "Appointment deleted"}
