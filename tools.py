import json
from crewai.tools import tool


@tool("alert_parser")
def alert_parser(alert_payload: str) -> dict:
    """Useful to parse alert JSON strings into structured dictionaries. 
    Accepts alert_payload as a JSON string."""
    return json.loads(alert_payload)


@tool("dependency_map")
def dependency_map(service_name: str) -> dict:
    """Useful to fetch the dependency graph for a specific service.
    Accepts service_name as a string."""
    return {
        "api-gateway": ["auth-service", "user-service", "payment-service"],
        "user-service": ["db-users", "cache"],
        "payment-service": ["db-payments", "third-party-gateway"],
    }


@tool("deployment_history")
def deployment_history(service_name: str = "all") -> list:
    """Useful to fetch recent deployment logs for services.
    Accepts optional service_name string."""
    return [
        {"service": "api-gateway", "version": "v2.1.3", "minutes_ago": 15},
        {"service": "payment-service", "version": "v5.4.1", "minutes_ago": 42},
    ]