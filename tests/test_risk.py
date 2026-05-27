from ai_agent_playbook.risk import RiskLevel, risk_gate


def test_high_risk_requires_approval():
    message = risk_gate(RiskLevel.HIGH, "send email")
    assert "Human approval" in message
