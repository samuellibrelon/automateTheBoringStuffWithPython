#! python3
#! pw.py - um programa para repositório de senhas que não é seguro


import sys
import pyperclip

PASSWORDS = {'email': 'gfdgjmklfodjgkjfdnbvçsdnfa345', 'game': 'fjasdk456', 'jureg': '4asda44'}

def main():
    if len(sys.argv) < 2:
        print("Usage: py main.py[account] - copy account password")
        sys.exit()

    account = sys.argv[1]  # The first argument from the command line is the account name

    if account in PASSWORDS:
        pyperclip.copy(PASSWORDS[account])
        print('Password for ' + account + ' copied to clipboard.')
    else:
        print('There is no account named ' + account)

if __name__ == "__main__":
    main()
