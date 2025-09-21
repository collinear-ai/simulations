from .calculate import Calculate
from .think import Think
from .find_customer_by_email import FindCustomerByEmail
from .find_customer_by_phone import FindCustomerByPhone
from .get_customer_details import GetCustomerDetails
from .get_service_details import GetServiceDetails
from .get_device_details import GetDeviceDetails
from .get_billing_details import GetBillingDetails
from .check_network_status import CheckNetworkStatus
from .manage_service import ManageService
from .troubleshoot_device import TroubleshootDevice
from .create_support_ticket import CreateSupportTicket
from .get_support_ticket_details import GetSupportTicketDetails
from .list_available_services import ListAvailableServices


ALL_TOOLS = [
    Calculate,
    Think,
    FindCustomerByEmail,
    FindCustomerByPhone,
    GetCustomerDetails,
    GetServiceDetails,
    GetDeviceDetails,
    GetBillingDetails,
    CheckNetworkStatus,
    ManageService,
    TroubleshootDevice,
    CreateSupportTicket,
    GetSupportTicketDetails,
    ListAvailableServices,
]
