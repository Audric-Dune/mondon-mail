import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os"],
                     "excludes": ["tkinter"],
                     "include_files": ["assets", "lib", "ui", "constant"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name="DUNE mail suivi production",
      version="2.0",
      description="Routine envoie mail suivi production",
      options={"build_exe": build_exe_options},
      executables=[Executable(script="main.py",
                              base=base,
                              icon="assets/mail.ico",
                              targetName="DUNE mail rapport production.exe")])
