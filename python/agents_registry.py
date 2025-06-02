# python/agents_registry.py
"""
Devuelve el agente principal creado por el framework (Agent 0)
"""

from agent import AgentContext


def get_main_agent():
    """
    Retorna el agente principal (Agent 0) del framework.
    Agent Zero usa call_subordinate para delegación, no sub_agents.
    """
    ctx = AgentContext.first()
    return ctx.agent0
