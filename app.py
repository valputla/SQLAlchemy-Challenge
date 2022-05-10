import numpy as np
import datetime as dt
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
    
@app.route("/api/v1.0/precipitation")
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

@app.route("/api/v1.0/stations")
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

@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    results = session.query(Measurement.date, Measurement.tobs).\
    filter(Measurement.station == "USC00519281").\
    filter(Measurement.date <= dt.date(2017, 8, 23)).\
    filter(Measurement.date >= dt.date(2016, 8, 23)).all()

    session.close()
    
    temp_list = []
    for temp in results:
        temp_dict = {}
        temp_dict["date"] = date
        temp_dict["tobs"] = temperature
        temp_list.append(temp_dict)
    return jsonify(temp_list)

    session.close()
    
    
@app.route("/api/v1.0/<start>")
def summary_stats_startdate(start):
    normalized_startdate = start.replace(" ", "").lower()
    for date in temp_list:
        search_term = date["start"].replace(" ", "").lower()

        if search_term == normalized_startdate:
            
            return jsonify(date)

    return jsonify({"error": "Character not found."}), 404






# When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than or equal to the start date.

# Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a given start or start-end range.






# /api/v1.0/<start>/<end>
# When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates from the start date through the end date (inclusive).







if __name__ == '__main__':
    app.run(debug=True)