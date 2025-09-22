import json
import os
from typing import Dict, Any

def load_data() -> Dict[str, Any]:
    """Load telehealth data from JSON files."""
    data_dir = os.path.dirname(__file__)
    
    # Load patients data
    with open(os.path.join(data_dir, "patients.json"), "r") as f:
        patients = json.load(f)
    
    # Load providers data
    with open(os.path.join(data_dir, "providers.json"), "r") as f:
        providers = json.load(f)
    
    # Load appointments data
    with open(os.path.join(data_dir, "appointments.json"), "r") as f:
        appointments = json.load(f)
    
    # Load medical records data
    with open(os.path.join(data_dir, "medical_records.json"), "r") as f:
        medical_records = json.load(f)
    
    return {
        "patients": patients,
        "providers": providers,
        "appointments": appointments,
        "medical_records": medical_records
    }