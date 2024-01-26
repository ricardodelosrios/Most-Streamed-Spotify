from dotenv import load_dotenv
import os
import base64
import requests  
import pandas as pd

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

def get_token():
    auth_string = f"{client_id}:{client_secret}"
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = base64.b64encode(auth_bytes).decode("utf-8")
    
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": f"Basic {auth_base64}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}

    result = requests.post(url, headers=headers, data=data)

    if result.status_code == 200:
        json_result = result.json()
        token = json_result.get("access_token")
        return token
    else:
        # Manejar el error de solicitud de manera apropiada
        print(f"Error en la solicitud de token: {result.status_code}")
        return None

token = get_token()

# Función para buscar una canción y obtener su ID
def search_track(track_name, artist_name, token):
    query = f"{track_name} artist:{artist_name}"
    url = f"https://api.spotify.com/v1/search?q={query}&type=track"
    response = requests.get(url, headers={'Authorization': f'Bearer {token}'})
    
    if response.status_code == 200:
        json_data = response.json()
        
        if 'items' in json_data.get('tracks', {}):
            items = json_data['tracks']['items']
            
            if items:
                first_result = items[0]
                track_id = first_result['id']
                return track_id

    # Si no hay resultados o hay algún otro problema
    print(f"No se encontraron resultados para la búsqueda: {query}")
    return None


# Función para obtener detalles de la canción
def get_track_details(track_id, token):
    url = f"https://api.spotify.com/v1/tracks/{track_id}"
    response = requests.get(url, headers={'Authorization': f'Bearer {token}'})
    
    if response.status_code == 200:
        json_data = response.json()
        try:
            image_url = json_data['album']['images'][0]['url']
            return image_url
        except KeyError:
            # Manejar el error de clave de manera apropiada
            return None
    else:
        # Manejar el error de solicitud de manera apropiada
        print(f"Error en la solicitud de detalles de pista: {response.status_code}")
        return None

# Leer el DataFrame (reemplazar 'your_file.csv' con la ruta de tu archivo CSV)
df_spotify = pd.read_csv('spotify-2023.csv', encoding='ISO-8859-1')

# Imprimir las columnas disponibles en el DataFrame
print(df_spotify.columns)

# Bucle a través de cada fila para obtener detalles de la pista y agregarlos al DataFrame
for i, row in df_spotify.iterrows():
    # Verificar si 'artist(s)_name' está presente en las columnas del DataFrame
    if 'artist(s)_name' in df_spotify.columns:
        track_id = search_track(row['track_name'], row['artist(s)_name'], token)
        if track_id:
            image_url = get_track_details(track_id, token)
            if image_url:
                df_spotify.at[i, 'image_url'] = image_url
    else:
        print("La columna 'artist(s)_name' no está presente en el DataFrame.")
        
# Guardar el DataFrame actualizado (reemplazar 'updated_file.csv' con el nombre de archivo de salida deseado)
df_spotify.to_csv('updated_file.csv', index=False)