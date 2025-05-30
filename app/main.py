from flask import Flask, request, jsonify
import requests
from dotenv import load_dotenv
import os
from pathlib import Path
from logger import get_logger
from responseError import response_error

env_path = Path(__file__).parent / 'secrets.env'
load_dotenv(dotenv_path=env_path)

logger = get_logger(__name__)

apiKey = os.getenv('API_KEY')

app = Flask(__name__)

@app.route('/deportes', methods=['GET'])
def servicios():
    logger.info("Se recibió una solicitud")

    if apiKey is None:
        logger.error("No se encontró API Key")
        return response_error(401, 'No se encontro API Key', 401)

    cat = request.args.get('categoria')
    if cat == 'argentina':
        url = 'https://api.the-odds-api.com/v4/sports/soccer_argentina_primera_division/odds?regions=us&apiKey=' + apiKey
        response = requests.get(url)

        if response.status_code != 200:
            response_data = response.json()
            logger.warning(f"La API externa retorno error: {response_data.get('error_code')}")
            return response_error(500, 'La API externa retorno error: ' + response_data.get('error_code'), 500)

        logger.info(f"Finalizo la solicitud")
        return jsonify({"resultado": response.json()})

    else:
        logger.warning(f"No hay resultados para la categoría: {cat}")
        return response_error(404, 'No hay resultados', 404)

if __name__ == '__main__':
    app.run(debug=True, port=5000)