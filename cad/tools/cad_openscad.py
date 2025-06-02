import subprocess
import uuid
import textwrap
import shutil
from pathlib import Path

STATIC_DIR = Path(__file__).resolve().parent.parent / ".." / "webui" / "cad"
STATIC_DIR.mkdir(parents=True, exist_ok=True)


def create_model(scad_code: str, fmt: str = "stl") -> str:
    uid = uuid.uuid4().hex
    scad = Path(f"/tmp/{uid}.scad")
    out = Path(f"/tmp/{uid}.{fmt}")

    scad.write_text(textwrap.dedent(scad_code))
    subprocess.run(["openscad", "-o", str(out), str(scad)], check=True)

    public = STATIC_DIR / out.name
    shutil.copy(out, public)
    return f"/cad/{out.name}"          # URL servida por Flask static
