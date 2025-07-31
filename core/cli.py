# core/cli.py

import click
from core.config import load_config  # Make sure core/config.py exists with load_config

@click.group()
def main():
    """Welcome to NexForge — ethical tools for empowered development."""
    pass

@main.command()
def hello():
    """Greet the user ethically."""
    click.echo("NexForge is ready to forge your future ethically!")

@main.command()
def config():
    """Display current NexForge configuration."""
    cfg = load_config()
    click.echo("🔐 Current NexForge Config:")
    for key, value in cfg.items():
        click.echo(f"  {key}: {value}")

if __name__ == "__main__":
    main()
