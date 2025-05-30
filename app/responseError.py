from flask import jsonify


def response_error(codigo, descripcion, http_status=500):
    error_body = {
        "codigo": str(codigo),
        "descripcion": descripcion
    }

    return jsonify(error_body), http_status