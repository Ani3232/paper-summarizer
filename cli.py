import click
from summerizer import summarize_paper


@click.command()
@click.argument("filepath")
@click.option("--model", default="qwen3.5:4b", show_default=True, help="Ollama model to use.")
@click.option("--style", default="detailed", show_default=True, type=click.Choice(["research","brief", "detailed", "bullet"]), help="The style of the summery.")
@click.option("--output", default=None, help="Save summery to a file instead of printing.")
@click.option("--chunk", is_flag=True, default=False, help="Chunk long papers before sending..")

def cli(filepath, model, style, output, chunk):
    """Summerize a research paper (.pdf or .txt)."""
    click.echo(f"♠ Loading: {filepath}")
    click.echo(f"♠ Model: {model} | Style: {style}")
    summarize_paper(filepath, model, style, output, chunk)

if __name__ == "__main__":
    cli()


# EXAMPLE
# python cli.py summerize paper.pdf --style bullet --output summary.md