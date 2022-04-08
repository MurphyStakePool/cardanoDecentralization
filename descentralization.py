#!/usr/bin/python3

import json, requests, itertools, argparse
from operator import itemgetter


parser = argparse.ArgumentParser(description='Cardano Descentralization')
parser.add_argument('-n', '--network', dest='network', type=str, help='testnet or mainnet', required=True)
parser.add_argument('-f', '--filter', dest='filter', type=str, help='state or continent', required=True)

args = parser.parse_args()

if (args.network not in ["mainnet","testnet"]):
    raise ValueError("use testnet or mainnet")

if (args.filter not in ["state","continent"]):
    raise ValueError("use state or continent")


#VARIABLES
if args.network == "mainnet":
    url = "https://explorer.mainnet.cardano.org/relays/topology.json"
    topology = requests.get(url)
    data = topology.json()
else:
    url = "https://explorer.cardano-testnet.iohkdev.io/relays/topology.json"
    topology = requests.get(url)
    data = topology.json()

#EXEC
if args.filter == "continent":
    relays_continent = sorted(data["Producers"], key=itemgetter("continent"))
    total=len(list(relays_continent))
    for country, continent in itertools.groupby(relays_continent, key=itemgetter("continent")):
        print(country, round((len(list(continent))/total*100),5), sep="|")
else:
    relays_state = sorted(data["Producers"], key=itemgetter("state"))
    total=len(list(relays_state))
    for country, state in itertools.groupby(relays_state, key=itemgetter("state")):
        print(country, round((len(list(state))/total*100),5), sep="|")

