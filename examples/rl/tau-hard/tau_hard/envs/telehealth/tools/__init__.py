from .find_patient_by_email import FindPatientByEmail
from .find_patient_by_name_dob import FindPatientByNameDOB
from .get_patient_details import GetPatientDetails
from .get_appointment_details import GetAppointmentDetails
from .get_provider_details import GetProviderDetails
from .list_available_providers import ListAvailableProviders
from .schedule_appointment import ScheduleAppointment
from .cancel_appointment import CancelAppointment
from .reschedule_appointment import RescheduleAppointment
from .calculate import Calculate
from .think import Think
from .transfer_to_human_support import TransferToHumanSupport


ALL_TOOLS = [
    FindPatientByEmail,
    FindPatientByNameDOB,
    GetPatientDetails,
    GetAppointmentDetails,
    GetProviderDetails,
    ListAvailableProviders,
    ScheduleAppointment,
    CancelAppointment,
    RescheduleAppointment,
    Calculate,
    Think,
    TransferToHumanSupport,
]