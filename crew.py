from crewai import Task, Crew, Process
from models import IncidentClassification, IncidentReport
from agents import create_all_agents

agents = create_all_agents()

task1 = Task(
    description=(
        "Analyze the following alert payload: {alert_payload}. "
        "Use the alert_parser tool to extract details. "
        "Classify the incident severity (P0-P4) and provide reasoning and key signals. "
        "Your output must perfectly match the IncidentClassification schema."
    ),
    agent=agents["incident_classifier"],
    expected_output="A JSON object matching the IncidentClassification schema with severity, reasoning, and key signals.",
    output_json=IncidentClassification
)

task2 = Task(
    description=(
        "Review the classified incident and the alert data {alert_payload}. "
        "Design a targeted Playwright-style smoke test plan to validate system health."
    ),
    agent=agents["api_test_strategist"],
    expected_output="A list of Playwright-style assertions describing the smoke test plan."
)

task3 = Task(
    description=(
        "Analyze the blast radius of the incident mentioned in {alert_payload}. "
        "Use dependency_map and deployment_history tools to identify affected services."
    ),
    agent=agents["blast_radius_analyst"],
    expected_output="A comprehensive list of impacted downstream services and components."
)

task4 = Task(
    description=(
        "Consolidate all findings from the previous tasks into a final incident report. "
        "Your output must perfectly match the IncidentReport schema."
    ),
    agent=agents["incident_commander"],
    expected_output="A complete incident report matching the IncidentReport schema.",
    output_json=IncidentReport
)

crew = Crew(
    agents=list(agents.values()),
    tasks=[task1, task2, task3, task4],
    process=Process.sequential,
    verbose=True
)