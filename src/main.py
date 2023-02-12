import typer
import pyfiglet
from _version import __version__

app = typer.Typer()


@app.command()
def version():
    print(f"{__version__}v")


if __name__ == "__main__":
    print(pyfiglet.figlet_format("Auto Setup"))
    app()
