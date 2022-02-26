import os
from flask import Flask
from cfenv import AppEnv
from hdbcli import dbapi

App = Flask(__name__)
env = AppEnv()

hana_service = 'hanatrial'
hana = env.get_service(label=hana_service)

@App.route('/')
def hello():
    if hana is None:
        return "Can't connect to HANA service '{}' – check service name?".format(hana_service)
    else:
        conn = dbapi.connect(address=hana.credentials['host'],
                             port=int(hana.credentials['port']),
                             user=hana.credentials['user'],
                             password=hana.credentials['password'],
                             encrypt='true',
                             sslTrustStore=hana.credentials['certificate'])

        cursor = conn.cursor()
        cursor.execute("select CURRENT_UTCTIMESTAMP from DUMMY")
        ro = cursor.fetchone()
        cursor.close()
        conn.close()

        return "Current time is: " + str(ro["CURRENT_UTCTIMESTAMP"])