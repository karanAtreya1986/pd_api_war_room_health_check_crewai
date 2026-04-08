from crewai import Agent, LLM
from tools import alert_parser, dependency_map, deployment_history

import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))
# Step 0 - set the llm. brain
groq_llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_LLM_KEY")
)


def create_incident_classifier():
    return Agent(
        role="Incident Classifier",
        goal="Classify severity of incidents using P0-P4 scale",
        backstory=(
            "You are an SRE expert responsible for rapid triage of production incidents. "
            "You analyze alert signals such as error rates, latency spikes, and affected users "
            "to assign accurate severity levels (P0-P4)."
        ),
        tools=[alert_parser],
        llm=groq_llm,
        verbose=True
    )


def create_api_test_strategist():
    return Agent(
        role="API Test Strategist",
        goal="Design immediate smoke tests for degraded APIs",
        backstory=(
            "You are a QA architect specializing in API reliability. "
            "You design fast, targeted smoke tests using Playwright-style syntax "
            "to validate system health during incidents."
        ),
        llm=groq_llm,
        verbose=True
    )


def create_blast_radius_analyst():
    return Agent(
        role="Blast Radius Analyst",
        goal="Identify impacted systems, flows, and dependencies",
        backstory=(
            "You are an expert in distributed systems and service dependency mapping. "
            "You evaluate cascading failures and determine downstream impacts "
            "using dependency graphs and deployment signals."
        ),
        tools=[dependency_map, deployment_history],
        llm=groq_llm,
        verbose=True
    )


def create_incident_commander():
    return Agent(
        role="Incident Commander",
        goal="Produce clear and actionable incident reports",
        backstory=(
            "You lead incident response war rooms. You synthesize technical findings "
            "into clear summaries, define mitigation steps, and communicate effectively "
            "with stakeholders."
        ),
        llm=groq_llm,
        verbose=True
    )


def create_all_agents():
    """Convenience factory to initialize all agents"""
    return {
        "incident_classifier": create_incident_classifier(),
        "api_test_strategist": create_api_test_strategist(),
        "blast_radius_analyst": create_blast_radius_analyst(),
        "incident_commander": create_incident_commander(),
    }