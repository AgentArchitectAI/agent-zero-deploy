from python.helpers.api import ApiHandler
from python.agents_registry import get_main_agent


class chat_cad(ApiHandler):
    """
    POST /chat_cad
    JSON { "message": "..." }
    """

    # ←– cambio aquí
    @classmethod
    def requires_auth(cls) -> bool:
        return False     # o True si quieres autenticación

    async def handle_request(self, request):
        msg = (request.json or {}).get("message", "")
        agent = get_main_agent()
        reply = agent.chat(msg)
        return {"response": reply}
