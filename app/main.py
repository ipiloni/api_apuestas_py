from flask import Flask, request
from apis.oddsAPI import obtenerApuestasDe, obtenerFutbol
from logger import get_logger

logger = get_logger(__name__)

app = Flask(__name__)

@app.route('/futbol', methods=['GET'])
def servicios():
    logger.info(f"Se recibió una solicitud")

    cat = request.args.get('liga')

    if cat is None:
        logger.info(f"Finalizo la solicitud")
        return obtenerFutbol()
    else:
        logger.info(f"Finalizo la solicitud")
        return obtenerApuestasDe(cat)


if __name__ == '__main__':
    app.run(debug=True, port=5000)