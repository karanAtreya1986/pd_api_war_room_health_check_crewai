import pytest
from crew import crew
import json

@pytest.mark.slow
def test_full_incident_flow():
    alert_payload_str = """
    {
        "endpoint": "/payments",
        "error_rate": 0.35,
        "latency_p99": 3200,
        "status_codes": {"500": 1200, "502": 300},
        "affected_users": 15000
    }
    """
    
    print("\n" + "="*50)
    print(f"🚨 SUBMITTING ALERT PAYLOAD:\n{alert_payload_str.strip()}")
    print("="*50 + "\n")

    result = crew.kickoff(inputs={"alert_payload": alert_payload_str})
    
    result_str = str(result)
    result_lower = result_str.lower()
    
    # Ensure severity present
    assert "severity" in result_lower

    # Ensure at least one action recommended
    assert "action" in result_lower or "mitigation" in result_lower

    print("\n" + "="*50)
    print("🎯 INTEGRATION TEST OUTPUT POINTERS:")
    try:
        # Assuming the final output was structured via output_json in CrewAI models
        if hasattr(result, 'pydantic') and result.pydantic:
            print(f"-> Severity Level: {result.pydantic.severity}")
            print(f"-> Recommended Action(s): {result.pydantic.immediate_actions}")
        elif hasattr(result, 'json_dict') and result.json_dict:
            # Another way CrewAI might expose it
            val = result.json_dict
            if type(val) == str:
                val = json.loads(val)
            print(f"-> Severity Level: {val.get('severity', 'Not Parsed')}")
            print(f"-> Recommended Action(s): {val.get('immediate_actions', 'Not Parsed')}")
        else:
            # Fallback string manipulation if pydantic payload unavailable
            import re
            severity_match = re.search(r"'severity':\s*'([^']+)'", result_str)
            action_match = re.search(r"'immediate_actions':\s*(\[[^\]]+\])", result_str)
            
            sev = severity_match.group(1) if severity_match else "Found in unstructured text"
            act = action_match.group(1) if action_match else "Found in unstructured text"
            
            print(f"-> Severity Level: {sev}")
            print(f"-> Recommended Action(s): {act}")
            print("\n-> Full Result Dump:\n" + result_str)
    except Exception as e:
        print(f"-> Raw Text Output (Extraction Failed [{e}]):\n{result_str}")
    print("="*50 + "\n")