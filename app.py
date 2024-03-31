from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db, load_job_from_db
from sqlalchemy import create_engine, text

app = Flask(__name__)


@app.route("/")
def front_page():
  return render_template('home.html',
                         jobs=load_jobs_from_db(),
                         company_name='Cicify')


@app.route("/api/jobs")
def get_list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(data=jobs, status=200, mimetype='application/json')


@app.route("/job/<id>")
def get_job(id):
  job = load_job_from_db(id)
  return render_template('jobpage.html', job=job)

@app.route("/job/<id>/apply", methods=["post"])
def apply_job(id):
  data = request.form
  job = load_job_from_db(id)
  return render_template('application_submited.html', application=data, job=job)
  



if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
