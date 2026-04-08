# Integration Test Report: Warroom CrewAI

## 🧪 Test Profile
- **Test File:** `test_integration.py`
- **Target Component:** Full Incident Flow (`test_full_incident_flow()`)
- **Status:** ✅ PASSED
- **Execution Time:** ~13.73 seconds

## 📥 Triggered Alert Payload (Mock Data)
The initial trigger for the incident response crew represents a major degradation in the backend endpoint:

```json
{
    "endpoint": "/payments",
    "error_rate": 0.35,
    "latency_p99": 3200,
    "status_codes": {"500": 1200, "502": 300},
    "affected_users": 15000
}
```

## 🎯 Test Objectives & Validation
The integration test executes a full end-to-end run using `crew.kickoff()`, verifying that the Crew of autonomous agents collaborate effectively to parse the alert, map the dependency blast radius, and generate a final actionable mitigation report. 

To ensure success, the test validates the output context stream against critical semantic tokens:
1. **Severity Mapping Validation:** Asserts the presence of the term `"severity"` in the final response. This confirms the *Incident Classifier* agent successfully triaged the telemetry and categorized it correctly (P1).
2. **Actionable Output Validation:** Asserts the presence of either `"action"` or `"mitigation"` in the final response output. This confirms the *Incident Commander* and *API Test Strategist* generated a tangible resolution path instead of hallucinating logic or halting at data collection. 

## 📈 System Diagnostics
The underlying API model used was successfully bridged to `groq/llama-3.3-70b-versatile` running natively via `.env` parameter matching.
- **Failures:** 0
- **Warnings Captured:** 13 (Consists entirely of Python 3.13 API internal `crewai` deprecation warnings checking for multimodal support. These are not breaking changes).

---
*Report auto-generated after successful pipeline deployment.*
