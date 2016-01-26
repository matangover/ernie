import os
from flask import Flask, request, Response, json
from pygtfs.gtfs_entities import Stop
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import text
from flask.ext.heroku import Heroku

app = Flask(__name__)
heroku = Heroku(app)
db = SQLAlchemy(app)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/stops")
def stops():
    lat, long = request.args["lat"], request.args["long"]
    #db.session.query(Stop).filter(text("ST_DWithin(ST_MakePoint(, :stop_long), 1000)"))
    #    .params("")
    distance_query = """ST_Distance(
        ST_SetSRID(ST_MakePoint(stop_lon, stop_lat), 4326)::geography,
        ST_SetSRID(ST_MakePoint(:long, :lat), 4326)::geography)"""

    stops = db.session.query(Stop).from_statement(text(
        """
        SELECT * FROM stops
        WHERE %(distance_query)s < 500
        ORDER BY %(distance_query)s
        LIMIT 5
        """ % {"distance_query": distance_query})).params(lat=lat, long=long)

    response = json.dumps([
        {
            "stop_id": stop.stop_id,
            "stop_code": stop.stop_code,
            "stop_name": stop.stop_name
        } for stop in stops])
    return Response(response=response, mimetype="application/json")

if __name__ == "__main__":
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get("PORT", 5000))
    debug = bool(os.environ.get("DEBUG", False))
    app.run(host="0.0.0.0", port=port, debug=debug)
