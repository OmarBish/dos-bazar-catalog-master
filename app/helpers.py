import requests
import sqlite3


from app import read_replicas

def updateReplicas(sqlite_query):
    body = {
            'sqlite_query':sqlite_query
        }
    for replica in read_replicas:
        requests.post(replica + "/master-notification" ,json=body)

def invalidateFrontendCache(body):
    
    body = {
        'base':'catalog',
        'route':'/query',
        'body':body
    }
    requests.post( "https://dos-bazar-front-end-server.herokuapp.com/cleare-cache" ,json=body)
        