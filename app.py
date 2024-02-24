from flask import Flask, render_template, request, redirect, abort, url_for, make_response
from dotenv import load_dotenv
import os
import pymongo
from pymongo import MongoClient

load_dotenv()

app = Flask(__name__)

uri = os.getenv("MONGO_URI")
db_name = os.getenv("MONGO_DBNAME")

# Create a new client and connect to the server
client = MongoClient(uri)
db = client[db_name]

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Connected to MongoDB!")
except Exception as e:
    print("MongoDB connection error:", e)

@app.route("/")
def home():
    return render_template('mainScreen.html')

# run the app
if __name__ == "__main__":
    FLASK_PORT = os.getenv("FLASK_PORT", "5000")
    app.run(port=FLASK_PORT)