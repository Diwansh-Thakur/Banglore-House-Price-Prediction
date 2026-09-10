import sys
from pathlib import Path

# Make the existing Flask application importable from Vercel's /api entrypoint.
ROOT = Path(__file__).resolve().parents[1]
SERVER_DIR = ROOT / "banglore" / "server"
if str(SERVER_DIR) not in sys.path:
    sys.path.insert(0, str(SERVER_DIR))

from server import app  # noqa: E402

# Vercel's Python runtime uses the WSGI application object above.
