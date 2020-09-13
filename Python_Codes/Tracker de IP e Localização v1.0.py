#Made by: Vinícius Azevedo
#Instagram: instagram.com/v.mazevedo
#Twitter: twitter.com/vmeazevedo

import requests
import json
import pprint

r = requests.get('http://www.geoplugin.net/json.gp')

if (r.status_code != 200):
    print('Não foi possível obter a localização.')
else:
    localizacao = json.loads(r.text)
    ip = json.loads(r.text)
    cidade = json.loads(r.text)
    regiao = json.loads(r.text)
    pais = json.loads(r.text)

    country = pais['geoplugin_countryName']
    region = regiao['geoplugin_region']
    city = cidade['geoplugin_city']
    ip_request = ip['geoplugin_request']
    lat = localizacao['geoplugin_latitude']
    long = localizacao['geoplugin_longitude']
    print('IP: ', ip_request)
    print('País: ', country)
    print('Estado: ', region)
    print('Cidade: ', city)
    print('lat: ',lat)
    print('lat: ', long)

input('\nPressione qualquer tecla para sair.')
