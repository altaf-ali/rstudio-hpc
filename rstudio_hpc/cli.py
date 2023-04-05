"""Console script for rstudio_hpc."""

import typer

app = typer.Typer()


@app.command()
def hello(name: str):
    """Handle CLI command 'hello'."""
    typer.echo(f"Hello {name}")


@app.command()
def goodbye(name: str, formal: bool = False):
    """Handle CLI command 'goodbye'."""
    if formal:
        typer.echo(f"Goodbye {name}. Have a good day.")
    else:
        typer.echo(f"Bye {name}!")


def main():
    """Main entrypoint."""
    app()


if __name__ == "__main__":
    main()  # pragma: no cover
