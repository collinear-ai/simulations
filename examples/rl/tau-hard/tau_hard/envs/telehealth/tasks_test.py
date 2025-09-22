from tau_bench.types import Task, Action

TASKS_TEST = [
    Task(
        annotator="0",
        user_id="sarah_johnson_1234",
        instruction="""
        You are Sarah Johnson, born March 15, 1985. 
        You want to schedule a follow-up appointment on Tuesday, September 23, 2025 at 10:00 AM 
        with your primary care doctor Dr. Garcia to discuss your blood pressure medication.
        """,
        actions=[
            Action(name="schedule_appointment", kwargs={"patient_id": "sarah_johnson_1234", "provider_id": "dr_garcia_primary", "date": "2025-09-23", "time": "10:00", "appointment_type": "follow_up"}),
        ],
        outputs= [],
    ),
    Task(
        annotator="1",
        user_id="david_martinez_5678",
        instruction="""
        You are David Martinez, email david.martinez@email.com. 
        You want to schedule a consultation appointment on Monday, September 22, 2025 at 2:00 PM (14:00) 
        with Dr. Smith (the cardiologist) to discuss your heart palpitations. However, if Dr. Smith is not 
        available at that exact time, you are willing to schedule with Dr. Garcia (your primary care doctor) 
        at the same time instead. You need to check both doctors' availability and schedules first.
        """,
        actions=[
            Action(name="find_patient_by_email", kwargs={"email": "david.martinez@email.com"}),
            Action(name="get_provider_details", kwargs={"provider_id": "dr_smith_cardiology"}),
            Action(name="get_provider_details", kwargs={"provider_id": "dr_garcia_primary"}),
            Action(name="schedule_appointment", kwargs={"patient_id": "david_martinez_5678", "provider_id": "dr_garcia_primary", "date": "2025-09-22", "time": "14:00", "appointment_type": "consultation"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="2",
        user_id="maria_rodriguez_4567",
        instruction="""
        You are Maria Rodriguez, born December 3, 1990. You have a complex scheduling situation:
        
        1. You currently have appointment APPT007 with Dr. Garcia on Monday, January 22nd 2025 at 9:00 AM
        2. You need to reschedule it because you have a work conflict, but you can only meet on the same day (Monday) at 3:00 PM or later.
        3. You also need to schedule a separate cardiology consultation for your new heart palpitations, preferably with the most experienced cardiologist available
        4. The cardiology appointment should be on Tuesday, January 23rd 2025, and you prefer morning appointments (before 12:00 PM)
        5. You want to verify your insurance copays for both appointments before confirming
        7. You need to get the meeting links for both final appointments
        
        Complete ALL requirements in the correct order, making decisions based on provider availability and experience.
        """,
        actions=[
            Action(name="reschedule_appointment", kwargs={"appointment_id": "APPT007", "new_date": "2025-01-22", "new_time": "15:00"}),
            Action(name="schedule_appointment", kwargs={"patient_id": "maria_rodriguez_4567", "provider_id": "dr_thompson_cardiology", "date": "2025-01-23", "time": "09:00", "appointment_type": "consultation"}),
        ],
        outputs=["20.00", "45.00", "https://telehealth.healthcenter.com/room/APPT007", "https://telehealth.healthcenter.com/room/APPT008"],
    ),
]
