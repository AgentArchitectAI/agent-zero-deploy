# python/tools/create_model.py
from python.helpers.tool import Tool
from cad.tools.cad_openscad import create_model as _create_model


class create_model(Tool):
    """
    Tool   : create_model
    Args   : scad_code (str), fmt (str, default "stl")
    Retorno: URL (o ruta) al archivo generado
    """

    async def execute(self, scad_code: str, fmt: str = "stl", **kwargs):
        print("✅ CAD-Engineer Tool activated with prompt:", scad_code)
        url = _create_model(scad_code, fmt)
        # break_loop=True hace que el agente responda inmediatamente
        return self.result(url, break_loop=True)
