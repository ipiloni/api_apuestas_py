from flask import jsonify


def response_error(codigo, descripcion, http_status):
    error_body = {
        "codigo": str(codigo),
        "descripcion": descripcion
    }

    return jsonify(error_body), http_status