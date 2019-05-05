import json
import os
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

BASE_DIR = os.path.dirname(os.getcwd()) if "src" in os.getcwd() else os.getcwd()
FILE = "config.json"

def carrega_sessao():
    CONFIG_FILE = f"{BASE_DIR}/{FILE}"
    with open(CONFIG_FILE) as json_file:
        data = json.load(json_file)

    nodes = data["NODES"].split(",")
    keyspace = data["KEYSPACE"]
#    user = data["USER"]
#    password = data["PASSWORD"]

#    auth_provider = PlainTextAuthProvider(username=str(user), password=str(password))
#    cluster = Cluster(nodes, auth_provider=auth_provider)
    cluster = Cluster(nodes)

    return cluster.connect(keyspace=keyspace)
