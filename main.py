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

def consultar(var):
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
t1 = threading.Thread(name="Hilo1", target=consultar, args=(1,))
t2 = threading.Thread(name="Hilo2", target=consultar, args=(1,))
t1.start()
t2.start()
t1.join()
t2.join()
tiempo_fin = datetime.datetime.now()
print("Tiempo transcurrido " + str(tiempo_fin.second - tiempo_ini.second))