import json
from typing import Any, Dict
from tau_bench.envs.tool import Tool

def troubleshoot_device(device_id: str, issue: str, data: dict) -> str:
    """
    Provide troubleshooting steps for device issues.
    
    Args:
        device_id: The device identifier
        issue: Description of the issue
        data: The loaded data dictionary
        
    Returns:
        Troubleshooting steps and recommendations
    """
    devices = data.get("devices", {})
    
    if device_id not in devices:
        return f"Device not found: {device_id}"
    
    device = devices[device_id]
    device_category = device.get("category", "")
    device_name = device.get("name", device_id)
    
    # Common troubleshooting steps based on device category and issue
    troubleshooting_steps = []
    
    issue_lower = issue.lower()
    
    if device_category == "mobile_phone":
        if any(keyword in issue_lower for keyword in ["slow", "data", "internet", "connection"]):
            troubleshooting_steps = [
                "1. Check if you're in an area with good signal coverage",
                "2. Turn airplane mode on for 30 seconds, then turn it off",
                "3. Restart your phone by powering it off and on",
                "4. Check if you've exceeded your data limit",
                "5. Reset network settings (this will remove saved WiFi passwords)",
                "6. Contact support if issue persists"
            ]
        elif any(keyword in issue_lower for keyword in ["call", "calling", "voice"]):
            troubleshooting_steps = [
                "1. Check signal strength - move to an area with better coverage",
                "2. Restart your phone",
                "3. Check if Do Not Disturb mode is enabled",
                "4. Verify the number you're calling is correct",
                "5. Try calling a different number to test",
                "6. Contact support for network issues"
            ]
        elif any(keyword in issue_lower for keyword in ["battery", "charging", "power"]):
            troubleshooting_steps = [
                "1. Try a different charging cable and adapter",
                "2. Clean the charging port gently with a dry brush",
                "3. Check if the device gets warm while charging",
                "4. Try charging from a different power source",
                "5. Restart the device",
                "6. If battery drains quickly, check for apps using excessive power"
            ]
        else:
            troubleshooting_steps = [
                "1. Restart your device",
                "2. Check for software updates",
                "3. Ensure you have adequate signal coverage",
                "4. Contact technical support for further assistance"
            ]
    
    elif device_category == "networking":
        if any(keyword in issue_lower for keyword in ["slow", "speed", "internet", "wifi", "connection"]):
            troubleshooting_steps = [
                "1. Unplug the router for 30 seconds, then plug it back in",
                "2. Check all cable connections are secure",
                "3. Move closer to the router if using WiFi",
                "4. Run a speed test from multiple devices",
                "5. Check for interference from other devices",
                "6. Reset router to factory settings if needed",
                "7. Contact support if speeds are consistently below plan speeds"
            ]
        elif any(keyword in issue_lower for keyword in ["not working", "no internet", "offline"]):
            troubleshooting_steps = [
                "1. Check that all cables are properly connected",
                "2. Look for any damaged cables",
                "3. Restart the router by unplugging for 30 seconds",
                "4. Check if the power LED is on",
                "5. Check if there are any service outages in your area",
                "6. Contact support if lights indicate a connection problem"
            ]
        else:
            troubleshooting_steps = [
                "1. Power cycle the router (unplug for 30 seconds)",
                "2. Check all cable connections",
                "3. Verify LED status lights",
                "4. Contact technical support if issue persists"
            ]
    
    elif device_category == "tv":
        if any(keyword in issue_lower for keyword in ["no signal", "black screen", "not working"]):
            troubleshooting_steps = [
                "1. Check that the TV is on the correct input/source",
                "2. Verify all cables are securely connected",
                "3. Restart the cable box by unplugging for 30 seconds",
                "4. Check if other channels work",
                "5. Ensure the TV is tuned to the right channel",
                "6. Contact support if no channels are working"
            ]
        elif any(keyword in issue_lower for keyword in ["remote", "control"]):
            troubleshooting_steps = [
                "1. Replace the batteries in the remote",
                "2. Point the remote directly at the device",
                "3. Remove any obstacles between remote and device",
                "4. Try using the buttons on the device itself",
                "5. Request a replacement remote if needed"
            ]
        elif any(keyword in issue_lower for keyword in ["quality", "pixelated", "freezing"]):
            troubleshooting_steps = [
                "1. Check all cable connections are tight",
                "2. Restart the cable box",
                "3. Check if the issue occurs on all channels",
                "4. Verify there are no service outages in your area",
                "5. Contact support for signal quality issues"
            ]
        else:
            troubleshooting_steps = [
                "1. Restart the device by unplugging for 30 seconds",
                "2. Check all connections",
                "3. Verify correct input/source selection",
                "4. Contact technical support for further assistance"
            ]
    
    else:
        troubleshooting_steps = [
            "1. Restart the device",
            "2. Check all connections and cables",
            "3. Verify power supply",
            "4. Contact technical support for device-specific assistance"
        ]
    
    result = f"""Troubleshooting Guide for {device_name}:

Issue: {issue}
Device Category: {device_category}

Recommended Steps:
"""
    
    for step in troubleshooting_steps:
        result += f"{step}\n"
    
    result += f"""
If these steps don't resolve the issue, please contact technical support with:
- Device ID: {device_id}
- Specific error messages (if any)
- When the issue started
- What you were doing when it occurred

Device Status: {device.get('status', 'Unknown')}
"""
    
    return result

class TroubleshootDevice(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], device_id: str, issue: str) -> str:
        devices = data.get("devices", {})
        
        if device_id not in devices:
            return f"Error: Device not found: {device_id}"
        
        device = devices[device_id]
        device_category = device.get("category", "")
        
        # Return standardized troubleshooting steps based on category
        if device_category == "mobile_phone":
            return "Troubleshooting steps: 1) Restart device 2) Check signal coverage 3) Reset network settings 4) Contact support if issue persists"
        elif device_category == "networking":
            return "Troubleshooting steps: 1) Unplug router for 30 seconds 2) Check cable connections 3) Run speed test 4) Contact support if needed"
        elif device_category == "tv":
            return "Troubleshooting steps: 1) Check correct input/source 2) Verify cable connections 3) Restart cable box 4) Contact support if needed"
        else:
            return "Troubleshooting steps: 1) Restart device 2) Check connections 3) Verify power supply 4) Contact support for assistance"

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "troubleshoot_device",
                "description": "Provide troubleshooting steps for device issues.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "device_id": {
                            "type": "string",
                            "description": "The device identifier, such as 'iphone_15_pro' or 'router_wifi6'.",
                        },
                        "issue": {
                            "type": "string",
                            "description": "Description of the issue with the device.",
                        },
                    },
                    "required": ["device_id", "issue"],
                },
            },
        }
