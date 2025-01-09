from zeep import Client
import certifi
import requests

# URL du WSDL
wsdl = 'https://itsupport.lemo.com/WebService/SmoBridge.php?wsdl'
response = requests.get(wsdl, verify=False)

# - pip install pip-system-certs
# https://itsupport.lemo.com/WebService/SmoBridge.php
#   https://itsupport.lemo.com/WebService/WebservicetestClient.php
# https://itsupport.lemo.com/WebService/SmoBridge.php?wsdl

# Initialisation du client SOAP
client = Client(wsdl=wsdl)

# Authentification
SESSION_ID= ''
LOGIN       = 'bvesy@lemo.com'
PASSWORD    =''
COMPANY_ACCOUNT = '40000'




# Appel de la méthode

response = client.service.EZV_SYS_OpenSession(SESSION_ID,LOGIN,PASSWORD,COMPANY_ACCOUNT)


#response = client.service.EZV_SYS_OpenSession(SESSION_ID,LOGIN,PASSWORD,COMPANY_ACCOUNT)

#response = client.service.loginRequest( User=username, Password=password)



# Affichage des résultats
for request in response.ServiceRequests:
    print("ID: {request.ID}, Title: {request.Title}, Status: {request.Status}")
