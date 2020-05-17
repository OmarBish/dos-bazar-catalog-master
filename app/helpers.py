import requests
import sqlite3


from app import read_replicas

def updateReplicas(sqlite_query):
    body = {
            'sqlite_query':sqlite_query
        }
    for replica in read_replicas:
        try:
            requests.post(replica + "/master-notification" ,json=body,timeout=0.001)
        except requests.exceptions.ReadTimeout:
            continue

def invalidateFrontendCache(query):
    
    body = {
        'base':'catalog',
        'route':'/query',
        'query':query
    }
    try:
        requests.post( "https://dos-bazar-front-end-server.herokuapp.com/cleare-cache" ,json=body,timeout=0.001)
    except requests.exceptions.ReadTimeout:
        return
        