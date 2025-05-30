## API Consulta Apuestas Deportivas Futbol Argentino
Esta API es una primer versión de una API realizada en Python.  
La misma llama a una API de Apuestas Deportivas y retorna sus resultados, manejando errores dentro de la misma.

La request a enviar debe tener el siguiente formato:  
http://localhost:5000/deportes?categoria=argentina

En caso OK retornara un JSON con la siguiente estructura:
```json
{
    "resultado": [
        {
            "away_team": "Platense",
            "bookmakers": [
                {
                    "key": "betrivers",
                    "last_update": "2025-05-30T11:29:28Z",
                    "markets": [
                        {
                            "key": "h2h",
                            "last_update": "2025-05-30T11:29:28Z",
                            "outcomes": [
                                {
                                    "name": "Atlético Huracán",
                                    "price": 2.43
                                },
                                {
                                    "name": "Platense",
                                    "price": 3.4
                                },
                                {
                                    "name": "Draw",
                                    "price": 2.85
                                }
                            ]
                        }
                    ],
                    "title": "BetRivers"
                },
                {
                    "key": "lowvig",
                    "last_update": "2025-05-30T11:29:20Z",
                    "markets": [
                        {
                            "key": "h2h",
                            "last_update": "2025-05-30T11:29:20Z",
                            "outcomes": [
                                {
                                    "name": "Atlético Huracán",
                                    "price": 2.55
                                },
                                {
                                    "name": "Platense",
                                    "price": 3.32
                                },
                                {
                                    "name": "Draw",
                                    "price": 2.8
                                }
                            ]
                        }
                    ],
                    "title": "LowVig.ag"
                }
            ],
            "commence_time": "2025-06-01T20:00:00Z",
            "home_team": "Atlético Huracán",
            "id": "6c6aec0308cca6ade06a52c7aa7cff7e",
            "sport_key": "soccer_argentina_primera_division",
            "sport_title": "Primera División - Argentina"
        }
    ]
}
```

En caso de Error, la API retornara el siguiente formato:

```json
{
"codigo": "401/404/500",
"descripcion": "Descripcion del error"
}
```

Fecha de modificación: 30/05/2025
Ignacio Piloni