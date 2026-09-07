from flask import Flask, jsonify, request
import logging

app = Flask(__name__)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

hotels = [
    {
        "id": 1,
        "name": "Minsk Central Hotel",
        "city": "Minsk",
        "room": "Standard",
        "price_per_night": 80
    },
    {
        "id": 2,
        "name": "Grand Palace Hotel",
        "city": "Minsk",
        "room": "Deluxe",
        "price_per_night": 120
    },
    {
        "id": 3,
        "name": "Riverside Hotel",
        "city": "Brest",
        "room": "Standard",
        "price_per_night": 65
    }
]


@app.route("/api/hotels", methods=["GET"])
def get_hotels():
    city = request.args.get("city")

    logger.info("GET /api/hotels request received")

    if city is not None:
        valid_cities = {hotel["city"] for hotel in hotels}

        if city not in valid_cities:
            logger.error("Invalid city parameter: %s", city)

            return jsonify({
                "error": "Invalid city parameter",
                "available_cities": sorted(valid_cities)
            }), 400

        filtered_hotels = [
            hotel for hotel in hotels
            if hotel["city"].lower() == city.lower()
        ]

        return jsonify({
            "city": city,
            "hotels": filtered_hotels
        })

    return jsonify({
        "hotels": hotels
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)