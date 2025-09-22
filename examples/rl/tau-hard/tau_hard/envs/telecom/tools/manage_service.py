import json
from typing import Any, Dict, Optional
from tau_bench.envs.tool import Tool

class ManageService(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str, action: str, service_id: Optional[str] = None) -> str:
        customers = data.get("customers", {})
        services = data.get("services", {})
        
        if customer_id not in customers:
            return f"Error: Customer not found: {customer_id}"
        
        customer = customers[customer_id]
        customer_services = customer.get("services", [])
        
        if action == "list":
            result = []
            for svc_id in customer_services:
                if svc_id in services:
                    svc = services[svc_id]
                    result.append({
                        "service_id": svc_id,
                        "name": svc.get('name', svc_id),
                        "monthly_price": svc.get('monthly_price', 0)
                    })
            return json.dumps({"customer_id": customer_id, "services": result})
        
        if not service_id:
            return f"Error: Service ID is required for action: {action}"
        
        if action == "add":
            if service_id not in services:
                return f"Error: Service not found: {service_id}"
            
            if service_id in customer_services:
                return f"Error: Customer {customer_id} already has service: {service_id}"
            
            # In a real system, this would modify the data
            service_name = services[service_id].get("name", service_id)
            return f"Success: Added service '{service_name}' to customer {customer_id}"
        
        elif action == "remove":
            if service_id not in customer_services:
                return f"Error: Customer {customer_id} does not have service: {service_id}"
            
            service_name = services.get(service_id, {}).get("name", service_id)
            return f"Success: Removed service '{service_name}' from customer {customer_id}"
        
        elif action == "suspend":
            if service_id not in customer_services:
                return f"Error: Customer {customer_id} does not have service: {service_id}"
            
            service_name = services.get(service_id, {}).get("name", service_id)
            return f"Success: Suspended service '{service_name}' for customer {customer_id}"
        
        elif action == "activate":
            if service_id not in customer_services:
                return f"Error: Customer {customer_id} does not have service: {service_id}"
            
            service_name = services.get(service_id, {}).get("name", service_id)
            return f"Success: Activated service '{service_name}' for customer {customer_id}"
        
        else:
            return f"Error: Invalid action: {action}. Valid actions are: add, remove, suspend, activate, list"

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "manage_service",
                "description": "Manage customer services: add, remove, suspend, activate, or list services.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "The customer's unique identifier, such as 'john_smith_1234'.",
                        },
                        "action": {
                            "type": "string",
                            "description": "Action to perform: 'add', 'remove', 'suspend', 'activate', or 'list'.",
                        },
                        "service_id": {
                            "type": "string",
                            "description": "Service identifier (required for add/remove/suspend/activate), such as 'mobile_unlimited'.",
                        },
                    },
                    "required": ["customer_id", "action"],
                },
            },
        }
