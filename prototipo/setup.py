import sys, os
from cx_Freeze import setup, Executable

setup(
    name="partsFinder",
    version="1.0",
    description="mpv",
    executables=[Executable("app.py", init_script='Console')],
    target_dir = os.path.dirname(os.path.abspath(__file__))
)
