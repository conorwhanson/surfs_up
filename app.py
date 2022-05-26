import numpy as np
import pandas as pd
import datetime as dt

import sqlalchemy
from sqlalchemy.orm import relationship,scoped_session,sessionmaker,aliased
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func
from flask import Flask, jsonify
################################################
#       SQL connection      #
# Set up SQLite database connection
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Create our session (link) from Python to the DB
SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

# define variables
Measurement = Base.classes.measurement
Station = Base.classes.station

# build the app
app = Flask(__name__)
app.session = scoped_session(SessionLocal)

@app.route('/')
def welcome():
    return(
    """Welcome to the Hawaii Climate Analysis API!<br/>
    """
    f"-------------------------------------------<br/>"
    f"Available Routes:<br/>"
    f"/api/v1.0/precipitation<br/>"
    f"/api/v1.0/stations<br/>"
    f"/api/v1.0/tobs<br/>"
    f"/api/v1.0/temp/start/end<br/>"
    ) 
    
@app.route('/api/v1.0/precipitation')
# get precipitation data, jsonify it to display on webpage
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = app.session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date,prcp in precipitation}

    return jsonify(precip)

@app.route('/api/v1.0/stations')

def stations():
    results = app.session.query(Station.station).all()
    stations = list(np.ravel(results))

    return jsonify(stations=stations)

@app.route('/api/v1.0/tobs')

def monthly_temp():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = app.session.query(Measurement.tobs).\
    filter(Measurement.station == 'USC00519281').\
    filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    
    return jsonify(temps=temps)

# final route will be able to run statistical analysis based on user input dates in url
@app.route('/api/v1.0/temp/<start>')
@app.route('/api/v1.0/temp/<start>/<end>')

def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)]

    if not end:
        results = app.session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = app.session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))

    return jsonify(temps)


if __name__ == '__main__':
    app.run(debug=True)