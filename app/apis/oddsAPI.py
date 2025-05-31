import logging
import requests
from app.logger import get_logger
from app.responseError import response_error
from app.config import get

logger = get_logger(__name__)

apiKey = get('API_KEY')

def obtenerFutbol():
    url = 'https://api.the-odds-api.com/v4/sports?apiKey=' + apiKey

    logger.info("API KEY " + apiKey)

    if apiKey is None:
        logger.error("No se encontró API Key")
        return response_error(401, 'No se encontro API Key', 401)

    response = requests.get(url)
    response_data = response.json()

    if response.status_code != 200:
        logging.warn('Hubo un error al llamar al servicio ObtenerDeportes: ' + response_data.get('error_code'))
        return response_error(500, 'La API externa retorno error: ' + response_data.get('error_code'), 500)
    else:
        soccer_items = [item for item in response_data if 'Soccer' in item['group']]
        return soccer_items

def obtenerApuestasDe(ligaDeFutbol):
    categoria = get(ligaDeFutbol)

    if apiKey is None:
        logger.error('No se encontró API Key')
        return response_error(401, 'No se encontro API Key', 401)

    if categoria is None:
        return response_error(404, 'No se encontro categoria habilitada', 404)

    url = 'https://api.the-odds-api.com/v4/sports/' + categoria + '/odds?regions=us&apiKey=' + apiKey

    response = requests.get(url)
    response_data = response.json()

    if response.status_code != 200:
        logging.warn('Hubo un error al llamar al servicio Obtener Apuestas de categoria: ' + response_data.get('error_code'))
        return response_error(500, 'La API externa retorno error: ' + response_data.get('error_code'), 500)
    else:
        return response_data

