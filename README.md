# Flask-app-on-SAP-BTP
Sample flask app with authorization and connected to CI/CD setup


## Setup Locally 

- Install python(3+), pip ,venv and vscode(or you can also choose editor of your choice like vscode) 
- checkout the source code.
- cd FLASK-APP-ON-SAP-BTP
- virtualenv venv
- .\venv\Scripts\activate
- pip install -r requirements.txt
- python run.py
- Visit the URL for conditions microservice documentation : http://127.0.0.1:5000/


Tutorial reference : https://developers.sap.com/tutorials/btp-cf-buildpacks-python-create.html

Note: Custom routes can also be created via manifest file if its in the account quota.

  routes:
    - route: python-1234567trial.cfapps.eu10.hana.ondemand.com