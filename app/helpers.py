import requests
import sqlite3


from app import read_replicas

def updateReplicas(sqlite_query):
    body = {
            'sqlite_query':sqlite_query
        }
    for replica in read_replicas:
        try:
            print("updating replica: "+ replica)
            requests.post(replica + "/master-notification" ,json=body,timeout=0.01)
        except requests.exceptions.ReadTimeout:
            continue

def invalidateFrontendCache(base):
    
    body = {
        'id':base,
    }
    try:    
        # requests.post( "http://127.0.0.1:3000"+"/cleare-cache" ,json=body,timeout=0.001)
        print("invalidate cache for: "+ base)
        requests.post( "https://dos-bazar-front-end-server.herokuapp.com/cleare-cache" ,json=body,timeout=0.01)
    except requests.exceptions.ReadTimeout:
        return
        