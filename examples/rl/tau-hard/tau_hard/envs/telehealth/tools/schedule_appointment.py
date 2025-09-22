from typing import Any, Dict
from tau_bench.envs.tool import Tool
import datetime

class ScheduleAppointment(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], patient_id: str, provider_id: str, date: str, time: str, 
             appointment_type: str) -> str:
        """Schedule a new appointment for a patient.
        
        Args:
            patient_id: The patient's unique identifier
            provider_id: The provider's unique identifier
            date: Appointment date in YYYY-MM-DD format
            time: Appointment time in HH:MM format (24-hour)
            appointment_type: Type of appointment (routine_checkup, follow_up, consultation, etc.)
            
        Returns:
            Success message with appointment ID, or error message if scheduling fails
        """
        patients = data["patients"]
        providers = data["providers"]
        appointments = data["appointments"]
        
        # Validate patient exists
        if patient_id not in patients:
            return f"Patient with ID {patient_id} not found."
            
        # Validate provider exists
        if provider_id not in providers:
            return f"Provider with ID {provider_id} not found."
        
        patient = patients[patient_id]
        provider = providers[provider_id]
        
        # Check if provider is available at the requested time
        try:
            appointment_date = datetime.datetime.strptime(date, "%Y-%m-%d")
            day_of_week = appointment_date.strftime("%A").lower()
            
            if day_of_week not in provider["schedule"]:
                return f"Provider {provider_id} does not work on {day_of_week.title()}."
                
            available_times = provider["schedule"][day_of_week]
            if time not in available_times:
                available_times_str = ', '.join(available_times) if available_times else 'None'
                return f"Provider {provider_id} is not available at {time} on {day_of_week.title()}. Available times: {available_times_str}"
                
        except ValueError:
            return f"Invalid date format: {date}. Please use YYYY-MM-DD format."
        
        # Check for conflicts with existing appointments
        for appt_id, appt in appointments.items():
            if (appt["provider_id"] == provider_id and 
                appt["date"] == date and 
                appt["time"] == time and 
                appt["status"] in ["scheduled", "pending_approval"]):
                return f"Provider {provider_id} already has an appointment scheduled at {time} on {date}."
        
        # Generate new appointment ID
        existing_ids = [int(appt_id.replace("APPT", "")) for appt_id in appointments.keys() if appt_id.startswith("APPT")]
        new_id_num = max(existing_ids) + 1 if existing_ids else 1
        new_appointment_id = f"APPT{new_id_num:03d}"
        
        # Determine copay amount based on provider specialty
        insurance = patient["insurance"]["primary"]
        if provider["specialty"] == "Primary Care":
            copay_amount = insurance["copay_primary"]
        else:
            copay_amount = insurance["copay_specialist"]
        
        # Create new appointment
        new_appointment = {
            "appointment_id": new_appointment_id,
            "patient_id": patient_id,
            "provider_id": provider_id,
            "date": date,
            "time": time,
            "duration_minutes": 30,  # Default duration
            "type": appointment_type,
            "status": "scheduled",
            "notes": "",
            "insurance_authorization": f"AUTH{new_id_num:06d}",
            "copay_amount": copay_amount,
            "meeting_link": f"https://telehealth.healthcenter.com/room/{new_appointment_id}"
        }
        
        # Add to appointments data
        appointments[new_appointment_id] = new_appointment
        
        patient_name = f"{patient['name']['first_name']} {patient['name']['last_name']}"
        provider_name = f"Dr. {provider['name']['last_name']}"
        
        return f"""Appointment successfully scheduled!

Appointment ID: {new_appointment_id}
Patient: {patient_name}
Provider: {provider_name} - {provider['specialty']}
Date: {date}
Time: {time}
Type: {appointment_type.replace('_', ' ').title()}
Copay: ${copay_amount:.2f}
Meeting Link: {new_appointment['meeting_link']}

Please save your appointment ID for future reference."""

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "schedule_appointment",
                "description": "Schedule a new telehealth appointment for a patient with a healthcare provider.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "patient_id": {
                            "type": "string",
                            "description": "The patient's unique identifier",
                        },
                        "provider_id": {
                            "type": "string",
                            "description": "The provider's unique identifier",
                        },
                        "date": {
                            "type": "string",
                            "description": "Appointment date in YYYY-MM-DD format",
                        },
                        "time": {
                            "type": "string",
                            "description": "Appointment time in HH:MM format (24-hour)",
                        },
                        "appointment_type": {
                            "type": "string",
                            "description": "Type of appointment (routine_checkup, follow_up, consultation, specialist_consultation, sick_visit)",
                        },
                    },
                    "required": ["patient_id", "provider_id", "date", "time", "appointment_type"],
                },
            },
        }
