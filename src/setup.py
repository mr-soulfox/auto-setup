import os
from cx_Freeze import setup, Executable
from _version import __version__

base = None

includes = ['typer']
packages = ['pyfiglet', 'inquirer']

setup(
    name="Auto Setup",
    description="Setup your development project environment",
    author="marcos paulo",
    url="https://github.com/mr-soulfox/AutoSetup",
    download_url="https://github.com/mr-soulfox/AutoSetup",
    license="MIT",
    version=__version__,
    executables=[Executable(script="src/main.py", target_name="AutoSetup",
                            base=base, icon="src/assets/favicon.ico")],
    options={
        "build_exe": {
            "include_msvcr": True,
            "packages": packages,
            "includes": includes
        }
    }
)

path = os.path.abspath(os.path.join(os.path.realpath(__file__), os.pardir))
build_path = os.path.join(path, "build")
