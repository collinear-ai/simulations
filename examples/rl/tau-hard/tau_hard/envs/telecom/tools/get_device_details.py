import json
from typing import Any, Dict
from tau_bench.envs.tool import Tool

class GetDeviceDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], device_id: str) -> str:
        devices = data.get("devices", {})
        
        if device_id not in devices:
            return f"Error: Device not found: {device_id}"
        
        return json.dumps(devices[device_id])

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_device_details",
                "description": "Get detailed information about a customer device.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "device_id": {
                            "type": "string",
                            "description": "The device identifier, such as 'iphone_15_pro' or 'router_wifi6'.",
                        },
                    },
                    "required": ["device_id"],
                },
            },
        }
