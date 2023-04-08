import requests

# Pedir al usuario el nombre de la ciudad
city = "new york"

# Definir la URL de la API y la clave de acceso
url = "https://api.openweathermap.org/data/2.5/weather"
# para que  te devuelva los datos solicitados necesitarás introducir tu api_key
api_key = "API_KEY"

# Realizar una solicitud GET a la API
response = requests.get(url, params={"q": city, "appid": api_key})

# Comprobar si la solicitud fue exitosa
if response.status_code == 200:
    # Extraer los valores de temperatura máxima y mínima del resultado JSON
    data = response.json()
    temp_max = data["main"]["temp_max"]
    temp_min = data["main"]["temp_min"]
    # Imprimir los resultados
    print(f"La temperatura máxima en {city} es {temp_max} Kelvin")
    print(f"La temperatura mínima en {city} es {temp_min} Kelvin")
else:
    # Imprimir un mensaje de error si la solicitud falló
    print("Error al obtener los datos de la API")