import os
from google.cloud.sql.connector import Connector, IPTypes
import pymysql
from flask import Flask, request, jsonify

# Environment variables (replace with your actual values)
INSTANCE_CONNECTION_NAME = os.environ.get("INSTANCE_CONNECTION_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")
DB_NAME = os.environ.get("DB_NAME")

# Create a connection pool using the Cloud SQL Python Connector
connector = Connector(IPTypes.PUBLIC)  # Or IPTypes.PRIVATE for private IP
def getconn() -> pymysql.connections.Connection:
    conn: pymysql.connections.Connection = connector.connect(
        INSTANCE_CONNECTION_NAME, "pymysql", user=DB_USER, password=DB_PASS, db=DB_NAME
    )
    return conn

engine = sqlalchemy.create_engine(
    "mysql+pymysql://", creator=getconn, pool_size=5, max_overflow=0
)

# Create a Flask app for API endpoints
app = Flask(__name__)

@app.route("/create", methods=["POST"])
def create():
    data = request.get_json()
    try:
        with engine.connect() as conn:
            result = conn.execute(sa.insert(test), data)
            conn.commit()
        return jsonify({"message": "Data created successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# ... Add similar routes for read, update, and delete operations

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
