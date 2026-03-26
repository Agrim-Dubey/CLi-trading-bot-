import typer
from rich.console import Console
from rich.table import Table
from bot.orders import place_order
from bot.logging_config import setup_logger

app = typer.Typer()
console = Console()
logger = setup_logger("cli")

@app.command()
def trade(
    symbol: str = typer.Option(..., help="Trading pair e.g. BTCUSDT"),
    side: str = typer.Option(..., help="BUY or SELL"),
    order_type: str = typer.Option(..., "--type", help="MARKET or LIMIT"),
    quantity: float = typer.Option(..., help="Order quantity"),
    price: float = typer.Option(None, help="Price required for LIMIT orders"),
):
    console.print("\n[bold cyan]Order Request Summary[/bold cyan]")
    console.print(f"  Symbol   : {symbol.upper()}")
    console.print(f"  Side     : {side.upper()}")
    console.print(f"  Type     : {order_type.upper()}")
    console.print(f"  Quantity : {quantity}")
    if price:
        console.print(f"  Price    : {price}")

    logger.info(f"Trade requested: {symbol} {side} {order_type} qty={quantity} price={price}")

    try:
        response = place_order(symbol, side, order_type, quantity, price)

        console.print("\n[bold green]Order Placed Successfully![/bold green]")

        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Field")
        table.add_column("Value")

        for field in ["orderId", "symbol", "side", "type", "status", "executedQty", "avgPrice"]:
            if field in response:
                table.add_row(field, str(response[field]))

        console.print(table)

    except ValueError as e:
        console.print(f"\n[bold red]Validation Error:[/bold red] {e}")
        logger.error(f"Validation error: {e}")
        raise typer.Exit(code=1)

    except Exception as e:
        console.print(f"\n[bold red]Order Failed:[/bold red] {e}")
        logger.error(f"Order failed: {e}")
        raise typer.Exit(code=1)

if __name__ == "__main__":
    app()