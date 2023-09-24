
import requests
from flask import Flask
app = Flask(__name__)

@app.get('/getAccesstoken')
def getAccessToken():
        url = 'http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/token'

        headers = {"Metadata-Flavor" : "Google"}
        response = requests.get(url, headers= headers)
        return response.json()
if __name__ == "__main__":
    app.run(host = '0.0.0.0',port = 8080, debug = False) 
