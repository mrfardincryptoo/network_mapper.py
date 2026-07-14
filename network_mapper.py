NETWORKS = {
    "Ethereum": 1,
    "Base": 8453,
    "Optimism": 10,
    "Arbitrum": 42161
}

def get_chain_id(name):
    return NETWORKS.get(name, "Unknown Network")

print(f"Chain ID for Base: {get_chain_id('Base')}")
