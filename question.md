Build a CrewAI crew that simulates a QA war room responding to an API health degradation incident. 

The crew has four agents. 

Agent 1 is an "Incident Classifier" who receives an alert payload (JSON string with endpoint, error_rate, latency_p99, status_codes, and affected_users count) and classifies the incident severity using the P0–P4 scale. 

Agent 2 is an "API Test Strategist" who designs an immediate smoke test plan — which endpoints to hit, what assertions to check, what headers/payloads to send — written as pseudocode that mirrors Playwright API testing syntax (apiContext.get(), expect(response).toBeOK()). 

Agent 3 is a "Blast Radius Analyst" who determines which downstream services, user flows, and scheduled jobs are impacted (use a custom @tool that returns a mock service dependency map). 

Agent 4 is a "Incident Commander" who synthesizes all three outputs into a single incident report with severity, blast radius, immediate actions, test plan, and communication draft for stakeholders. 

Use Process.sequential with proper context chaining across all four tasks. Create at least 3 custom tools (alert parser, dependency map, recent deployment history). 

Define two Pydantic models — IncidentClassification and IncidentReport — and use output_json on Tasks 1 and 4 respectively. 

Write a full pytest test suite: unit tests for all tools, configuration tests for all agents, and one integration test (marked @pytest.mark.slow) that runs the complete crew against a sample alert payload and asserts the output contains a severity level and at least one recommended action.