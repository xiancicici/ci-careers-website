from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://avnadmin:AVNS_PiD51pD5xwoJxwnfFmd@cici-berkeley-e360.a.aivencloud.com:25746/cicidb?charset=utf8mb4"

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                           "ssl_ca": "/etc/ssl/cert.pem"
                       }})

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs")).mappings().all()
    return result
