import pandas as pd
import numpy as np
import datetime as dt


import sqlalchemy

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

engine = create_engine("sqlite:///hawaii.sqlite")

engine.execute(SELECT * FROM Measurement LIMIT 5).fetchall()

# reflect an existing database into a new model
# Base = automap_base()
# reflect the tables
# Base.prepare(engine, reflect=True)

# Measurement=Base.classes.measurement
# Station=Base.classes.station

session = Session(engine)

app = Flask(__name__)


@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"/api/v1.0/precipitation"
        f"api/v1.0/stations"
        f"/api/v1.0/tobs"
        f"//api/v1.0/<start>"
        f"/api/v1.0/<start>/<end>"
    )



if __name__ == '__main__':
    app.run(debug=True)