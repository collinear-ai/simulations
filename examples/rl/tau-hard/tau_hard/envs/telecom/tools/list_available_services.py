import json
from typing import Any, Dict, Optional
from tau_bench.envs.tool import Tool

class ListAvailableServices(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], category: Optional[str] = None) -> str:
        """
        List available services, optionally filtered by category.
        
        Args:
            category: Optional service category to filter by ("mobile", "internet", "tv", "phone", "security")
            data: The loaded data dictionary
            
        Returns:
            List of available services as a formatted string
        """
        services = data.get("services", {})
        
        if not services:
            return "No services available"
        
        valid_categories = ["mobile", "internet", "tv", "phone", "security"]
        
        if category and category not in valid_categories:
            return f"Invalid category: {category}. Valid categories: {', '.join(valid_categories)}"
        
        result = "Available Services:\n"
        
        # Group services by category
        services_by_category = {}
        for service_id, service_info in services.items():
            svc_category = service_info.get("category", "other")
            if svc_category not in services_by_category:
                services_by_category[svc_category] = []
            services_by_category[svc_category].append((service_id, service_info))
        
        # Display services
        for cat in sorted(services_by_category.keys()):
            if category and cat != category:
                continue
                
            result += f"\n{cat.upper()} SERVICES:\n"
            
            for service_id, service_info in sorted(services_by_category[cat], key=lambda x: x[1].get('monthly_price', 0)):
                name = service_info.get('name', service_id)
                price = service_info.get('monthly_price', 0)
                description = service_info.get('description', 'No description available')
                
                result += f"\n• {name} (${price:.2f}/month)\n"
                result += f"  ID: {service_id}\n"
                result += f"  {description}\n"
                
                # Add category-specific details
                if cat == 'mobile':
                    data_limit = service_info.get('data_limit', 'N/A')
                    speed = service_info.get('speed', 'N/A')
                    result += f"  Data: {data_limit}, Speed: {speed}\n"
                
                elif cat == 'internet':
                    download_speed = service_info.get('speed_download', 'N/A')
                    upload_speed = service_info.get('speed_upload', 'N/A')
                    technology = service_info.get('technology', 'N/A')
                    result += f"  Speed: {download_speed}↓/{upload_speed}↑, Technology: {technology}\n"
                
                elif cat == 'tv':
                    channels = service_info.get('channel_count', 'N/A')
                    dvr = service_info.get('dvr_hours', 'N/A')
                    result += f"  Channels: {channels}, DVR: {dvr} hours\n"
                
                elif cat == 'phone':
                    lines = service_info.get('line_count', 'N/A')
                    international = service_info.get('international_calling', False)
                    result += f"  Lines: {lines}, International: {'Yes' if international else 'No'}\n"
                
                elif cat == 'security':
                    monitoring = service_info.get('monitoring', False)
                    equipment = service_info.get('equipment_included', False)
                    result += f"  24/7 Monitoring: {'Yes' if monitoring else 'No'}, Equipment: {'Included' if equipment else 'Not included'}\n"
        
        if category and category not in services_by_category:
            result += f"\nNo services available in category: {category}"
        
            # Return all services or filtered by category
            services = data.get("services", {})
            
            if category:
                filtered_services = {k: v for k, v in services.items() if v.get("category") == category}
                return json.dumps(filtered_services)
            
            return json.dumps(services)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_available_services",
                "description": "List available services, optionally filtered by category.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "category": {
                            "type": "string",
                            "description": "Optional service category to filter by: 'mobile', 'internet', 'tv', 'phone', or 'security'.",
                        },
                    },
                    "required": [],
                },
            },
        }
