from rich import print

from rich.console import Console
from speedtest import Speedtest

console = Console()
st = Speedtest()

with console.status("[bold green]Замеряю скорость интернета...") as status:
    dl_speed = int(st.download() / 8000)
    up_speed = int(st.upload() / 8000)

print(f"[bold bright_blue]Скорость закачки: {dl_speed} kb/s[/bold bright_blue]\\\
    \n[bold red3]Скорость выгрузки: {up_speed} kb/s[/bold red3]")
import time
while True:
    print("salom")  # типа отправляешь сообщение
    time.sleep(2)
