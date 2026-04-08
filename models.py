from pydantic import BaseModel, Field
from typing import List, Dict, Any


class IncidentClassification(BaseModel):
    severity: str = Field(..., description="P0–P4 severity level")
    reasoning: str = "Triage in progress"
    key_signals: Dict[str, Any] = {}


class IncidentReport(BaseModel):
    severity: str = "Unknown"
    summary: str = "Report pending"
    blast_radius: List[str] = []
    impacted_services: List[str] = []
    immediate_actions: List[str] = []
    test_plan: str = "No plan generated"
    communication: str = "Draft pending"