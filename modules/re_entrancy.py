import click
import re
from modules.utils.parse_contract_util import parse_contract
from modules.utils.printer import *
from vulnerabilities_descriptions.reentrancy_desc import *

def reentrancy(contract):
    r = re.compile(r'(payable\(.*?\)\.transfer\(.*?\);.*?balance\[.*?\]\s*?=.*?)', re.MULTILINE | re.DOTALL)
    parsed_contract_into_list = parse_contract(contract)
    newlist = list(filter(r.finditer, parsed_contract_into_list))

    newlist_to_print = []
    if newlist:
        for match in newlist:
            line_number = 1 + parsed_contract_into_list.index(match.string)
            line_number_as_str = str(line_number)
            newlist_to_print.append(line_number_as_str)

        newlist_printable = ', '.join(newlist_to_print)
        printer_vuln(newlist_printable, vulnerability_name, vulnerability_description, vulnerability_recommendation, more_info)
