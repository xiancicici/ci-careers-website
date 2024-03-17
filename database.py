from sqlalchemy import create_engine, text
import os

AIVEN_DB_PASS = os.getenv('AIVEN_DB_PASS')
db_connection_string = f"mysql+pymysql://avnadmin:{AIVEN_DB_PASS}@cici-berkeley-e360.a.aivencloud.com:25746/cicidb?charset=utf8mb4"

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                           "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs")).mappings().all()
    return result