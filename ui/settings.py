import pathlib
import tempfile

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent
TEMP_DIR = pathlib.Path(tempfile.gettempdir()) / "photo_decorator"
TEMP_DIR.mkdir(exist_ok=True)
CONFIG_FILE = (TEMP_DIR / 'config').__str__()
