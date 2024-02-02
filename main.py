from eth_account import Account


def all_lines(filepath: str):
    with open(filepath, 'r') as file:
        lines = file.readlines()

    if not lines:
        return False
    return lines


def add_line(filepath: str, line: str):
    with open(filepath, 'a') as file:
        file.write(line + '\n')


def clear_file(filepath: str):
    with open(filepath, 'w') as file:
        file.truncate(0)


action = int(input('[1] mnemonic -> private key\n[2] private key -> address\n[3] mnemonic -> address\n\n> '))

if action == 1:
    mnemonics = all_lines(filepath="mnemonics.txt")
    if mnemonics:
        clear_file(filepath="private_keys.txt")
        Account.enable_unaudited_hdwallet_features()
        for mnemonic in mnemonics:
            account = Account.from_mnemonic(mnemonic.strip())
            add_line(filepath="private_keys.txt", line=account.key.hex())

elif action == 2:
    private_keys = all_lines(filepath="private_keys.txt")
    if private_keys:
        clear_file(filepath="addresses.txt")
        for private_key in private_keys:
            account = Account.from_key(private_key.strip())
            add_line(filepath="addresses.txt", line=account.address)

elif action == 3:
    mnemonics = all_lines(filepath="mnemonics.txt")
    if mnemonics:
        clear_file(filepath="addresses.txt")
        Account.enable_unaudited_hdwallet_features()
        for mnemonic in mnemonics:
            account = Account.from_mnemonic(mnemonic.strip())
            add_line(filepath="addresses.txt", line=account.address)
