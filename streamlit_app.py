from pathlib import Path
import runpy


APP_PATH = Path(__file__).with_name("dashboard_app 3.py")
runpy.run_path(str(APP_PATH), run_name="__main__")
