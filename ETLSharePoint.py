import requests
from requests.auth import HTTPBasicAuth

# Defina suas credenciais
username = "svc-sede-spfarm@infraero.gov.br"
password = "W*9%$?WnFQ"
admin_url = "https://infraerogovbr-admin.sharepoint.com/"

# URL para recuperar todos os sites
sites_url = f"{admin_url}/_api/search/query?querytext='contentclass:STS_Site'&selectproperties='Title,Path'"

# Faça uma solicitação para obter os sites
response = requests.get(sites_url, auth=HTTPBasicAuth(username, password))

# Verifique se a solicitação foi bem-sucedida
if response.status_code == 200:
    data = response.json()

    # Itere sobre os resultados e imprima as informações
    for site in data["PrimaryQueryResult"]["RelevantResults"]["Table"]["Rows"]:
        site_title = next((prop["Value"] for prop in site["Cells"] if prop["Key"] == "Title"), None)
        site_url = next((prop["Value"] for prop in site["Cells"] if prop["Key"] == "Path"), None)
        print("Title:", site_title)
        print("URL:", site_url)
        print("---------------------------")
else:
    print("Falha ao recuperar os sites. Status code:", response.status_code)
