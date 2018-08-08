import threading
import time
import datetime
import requests
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
url = config['XSENGINE']['URL']
user = config['XSENGINE']['USERNAME']
pas = config['XSENGINE']['PASSWORD']

def consultar():
    try:
        for i in range(0,100):
            querystring = {
                "cmd": "select",
                "query": 'SELECT TOP 100 * FROM OLIVOS_SEBAS.OCRD'
            }
            response = requests.get(url=url, params=querystring,auth=(user,pas))
        return
    except Exception as e:
        return str(e)


tiempo_ini = datetime.datetime.now()
consultar()
consultar()
tiempo_fin = datetime.datetime.now()
print("Tiempo transcurrido " + str(tiempo_fin.second - tiempo_ini.second))