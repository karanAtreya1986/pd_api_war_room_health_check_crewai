from agents import create_all_agents


def test_agents_creation():
    agents = create_all_agents()

    assert "incident_classifier" in agents
    assert "api_test_strategist" in agents
    assert "blast_radius_analyst" in agents
    assert "incident_commander" in agents


def test_agent_roles():
    agents = create_all_agents()

    assert agents["incident_classifier"].role == "Incident Classifier"
    assert agents["incident_commander"].role == "Incident Commander"


def test_tools_attached():
    agents = create_all_agents()

    classifier_tools = [t.name for t in agents["incident_classifier"].tools]
    assert "alert_parser" in classifier_tools

    blast_tools = [t.name for t in agents["blast_radius_analyst"].tools]
    assert "dependency_map" in blast_tools
    assert "deployment_history" in blast_tools