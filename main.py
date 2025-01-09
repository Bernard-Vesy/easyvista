from zeep import Client

# URL du WSDL
wsdl = 'https://your-instance.easyvista.com/EasyVista/api.svc?wsdl'

# Initialisation du client SOAP
client = Client(wsdl=wsdl)

# Authentification
username = 'your_username'
password = 'your_password'

# Appel de la méthode
response = client.service.GetServiceRequests(User=username, Password=password)

# Affichage des résultats
for request in response.ServiceRequests:
    print(f"ID: {request.ID}, Title: {request.Title}, Status: {request.Status}")
