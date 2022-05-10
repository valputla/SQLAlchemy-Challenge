import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify


engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station

app = Flask(__name__)


# @app.route("/")
# def home():
#     f"Welcome to the Climate app API!<br>"
#     f"Available routes:<br/>"
#     f"/api/v1.0/precipitation<br/>"
#     f"/api/v1.0/stations<br/>"
#     f"/api/v1.0/tobs<br/>"
#     f"/api/v1.0/<start>/<br/>"
#     f"/api/v1.0/<start>/<end>"
    
@app.route("/precipitation")
def precipitation():
    session = Session(engine)
    results = session.query(Measurement.date, Measurement.prcp).all()
    
    session.close()
    
    date_prcp = []
    for date, precipitation in results:
        date_prcp_dict = {}
        date_prcp_dict["date"] = date
        date_prcp_dict["prcp"] = precipitation
        date_prcp.append(date_prcp_dict)
    return jsonify(date_prcp)

@app.route("/stations")
def stations():
    session = Session(engine)
    results = session.query(Station.station).all()
    
    session.close()
    
    station_list = []
    for station in results:
        station_dict = {}
        station_dict["station"] = station
        station_list.append(station_dict)
    return jsonify(station_list)

/api/v1.0/stations

Return a JSON list of stations from the dataset.

if __name__ == '__main__':
    app.run(debug=True)