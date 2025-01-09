from zeep import Client

# URL du WSDL
wsdl = 'https://itsupport.lemo.com/WebService/SmoBridge.php?wsdl'

# Initialisation du client SOAP
client = Client(wsdl=wsdl)

# Authentification
username = 'bvesy@lemo.com'
password = 'Koala74-74-74'

# Appel de la méthode
response = client.service.GetServiceRequests(User=username, Password=password)

# Affichage des résultats
for request in response.ServiceRequests:
    print(f"ID: {request.ID}, Title: {request.Title}, Status: {request.Status}")
