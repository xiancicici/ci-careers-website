from flask import Flask, render_template, jsonify
from database import load_jobs_from_db
from sqlalchemy import create_engine, text

app = Flask(__name__)



@app.route("/")
def front_page():
    return render_template('home.html', 
                           jobs=load_jobs_from_db(), 
                           company_name='Cicify')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(load_jobs_from_db())

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)