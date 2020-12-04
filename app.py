import pandas as pd
import numpy as np
import datetime as dt


import sqlalchemy

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


engine = create_engine("sqlite:///hawaii.sqlite")


# engine.execute(SELECT * FROM Measurement LIMIT 5).fetchall()

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
print(Base.classes.keys())

Measurement=Base.classes.measurement
Station=Base.classes.station

app = Flask(__name__)



@app.route("/")
def welcome():
    """List all available api routes."""
    
    return (
        f"/api/v1.0/precipitation <br>"
        f"api/v1.0/stations <br>"
        f"/api/v1.0/tobs <br>"
        f"//api/v1.0/<start> <br>"
        f"/api/v1.0/<start>/<end> <br>"
    )

@app.route("/api/v1.0/precipitation")

def precipitation():
    session = Session(engine)
    results=session.query(Measurement.date,Measurement.prcp).all()
    session.close()
    all_dates=[]
    for date,prcp in results:
        all_dates_dic={}
        all_dates_dic["date"]=date
        all_dates_dic["prcp"]=prcp
        all_dates.append(all_dates_dic)

    return (
        jsonify(all_dates)
    )


@app.route("/api/v1.0/stations")

def stationsapp():
    session = Session(engine)
    results1=session.query(Station.station,Station.name).all()
    session.close()
    all_stations=[]
    for station,name in results1:
        all_stations_dic={}
        all_stations_dic["station"]=station
        all_stations_dic["name"]=name
        all_stations.append(all_stations_dic)

    return (
        jsonify(all_stations)
    )



@app.route("/api/v1.0/tobs")

def tobs():
 
    session = Session(engine)
    results3=session.query(Measurement.date,Measurement.tobs).filter(Measurement.station== 'USC00519523').filter(Measurement.date>=('2017,8,23')).all()
    session.close()
    temps=[]

    for date,tobs in results3:
        temps_dic={}
        temps_dic["date"]=date
        temps_dic["tobs"]=tobs
        temps.append(temps_dic)

    return (
        jsonify(temps)
    )


@app.route("/api/v1.0/start/<start>")

def calc_temps(start):
    session = Session(engine)
    
    results6= session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).all()

    session.close()

    return (
        jsonify(results6)
    )
@app.route("/api/v1.0/start_end/<start>/<end>")

def start_end(start,end):

    session = Session(engine)
    
    results7= session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).filter(Measurement.date <= end).all()

    session.close()

    return (
        jsonify(results7)
    )

#     return (
#         jsonify(hello_dic)
#     )

if __name__ == '__main__':
    app.run(debug=True)