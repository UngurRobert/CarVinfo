import requests
import os
from dotenv import load_dotenv

def getInfoByVin(vin):
    load_dotenv()
    token = os.getenv("KEYcar")
    url = "https://car-api2.p.rapidapi.com/api/vin/"+vin

    headers = {
        "X-RapidAPI-Key":token,
        "X-RapidAPI-Host": "car-api2.p.rapidapi.com"
    }

    return requests.get(url, headers=headers).json()
   
def GetPhotos(query):
    load_dotenv()
    token = os.getenv("keyphoto")
   
    url="https://api.unsplash.com/search/photos"
    params = {
        "query": query,
        "per_page": 3 
    }
    headers = {
        "Authorization": "Client-ID " + token
    }
    response = requests.get(url, params=params, headers=headers).json()
    photos=[]
    for result in response["results"]:
        photos.append(result['urls']['regular'])
    return photos