import pytest
from tools import alert_parser, dependency_map, deployment_history


def test_alert_parser():
    payload = '{"endpoint":"/api","error_rate":0.2}'
    result = alert_parser.run(payload)
    assert result["endpoint"] == "/api"


def test_dependency_map():
    result = dependency_map.run("api-gateway")
    assert "auth-service" in result["api-gateway"]


def test_deployment_history():
    result = deployment_history.run("")
    assert len(result) > 0
    assert "service" in result[0]