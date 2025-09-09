import pyfiglet
import click
from termcolor import colored

def print_banner(contract_name):
    banner = pyfiglet.figlet_format("inspectQL")
    print(banner)
    click.echo(f'''smart contracts vulnerability detector \n

whatever
''')
    print("Scanning "+colored(f"{contract_name}", attrs=['bold'])+" in progress.\nPlease see results below.\n")

