from web3 import Web3
import time

# Connect to the Ethereum network using RPC endpoint
w3 = Web3(Web3.HTTPProvider('https://eth1.lava.build/lava-referer-f3d85741-b32d-4c1c-8e2e-4091d4fcb05d/'))

def report_gas():
    latest_block = w3.eth.getBlock('latest')
    gas_limit = latest_block.gasLimit
    gas_used = latest_block.gasUsed
    print(f"Gas Limit: {gas_limit}, Gas Used: {gas_used}")

while True:
    report_gas()
    time.sleep(15)
