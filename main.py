import click
import re
import time
import random
import pyfiglet
import os

from modules.floating_pragma import * 
from modules.utils.parse_contract_util import parse_contract  
from modules.re_entrancy import *  
from modules.utils.remove_comments import *
from modules.utils.banner import * 
from modules.unchecked_external_call import *

@click.group()
def mycommands():
    pass

def update_bar(progress_bar_iterator):
    progress_bar_iterator.update(1)
    print("\n")
    time.sleep(0.1)

@click.command('scan', help="scan contract")
@click.argument('contract', type=click.Path(exists=True), required=1)
def scan_contract(contract):  
    print_banner(contract)  
    with click.progressbar(length=5, label="SCANNING") as bar:
        print("\n")
        for i in range(5):
            pass
            update_bar(bar)
        print('''
======================================
              RESULTS
======================================
        ''')

        try:
            floating_pragma(contract)
        except:
            print("An error occured while checking floating pragma. This vulnerability class was NOT checked.")


        try:
            parsed_contract = parse_contract(contract)
            reentrancy(''.join(parsed_contract))
        except:
            print("An error occurred while checking reentrancy. This vulnerability class was NOT checked.")

        click.echo("Scan completed. See results above.")

        try:
            unchecked_external_call(contract)
        except:
            print("An error occured while checking unchecked external call. This vulnerability class was NOT checked.")

mycommands.add_command(scan_contract)

if __name__ == '__main__':
    mycommands()

