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


@app.route("/")
def home():
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end"
    )

 
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
    results = session.query(Station.station, Station.name).all()
    
    session.close()

    station_list = []
    for station in results:
        station_dict = {}
        station_dict["station id"] = station[0]
        station_dict["station name"] = station[1]
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
        temp_dict["date"] = temp[0]
        temp_dict["tobs"] = temp[1]
        temp_list.append(temp_dict)
    return jsonify(temp_list)
    
    
@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def temp(start = None, end = None):
    session = Session(engine)
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    results = session.query(*sel).filter(func.strftime(Measurement.date) >= start).filter(func.strftime(Measurement.date) <= end).all()
    
    session.close()    
    
    temp_tobs = []
    for tmin, tavg, tmax in results:
        temp_tobs_dict = {}

        temp_tobs_dict[0] = tmin
        temp_tobs_dict[1] = tavg
        temp_tobs_dict[2] = tmax

        temp_tobs.append(temp_tobs_dict)
    return jsonify(temp_tobs)


## If statement - if the user does not provide anything then we need to provide a date. If end is = None then... else... continue with for loop.

# /api/v1.0/<start> and /api/v1.0/<start>/<end>


# Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a given start or start-end range.



# When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates from the start date through the end date (inclusive).

# def calc_temps(start_date, end_date):
#     """TMIN, TAVG, and TMAX for a list of dates.
    
#     Args:
#         start_date (string): A date string in the format %Y-%m-%d
#         end_date (string): A date string in the format %Y-%m-%d
        
#     Returns:
#         TMIN, TAVE, and TMAX
#     """
    
#     return session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
#         filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()

# # For example
# print(calc_temps('2012-02-28', '2012-03-05'))

# Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a given start or start-end range.

# /api/v1.0/<start>/<end>
# When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates from the start date through the end date (inclusive).



if __name__ == '__main__':
    app.run(debug=True)