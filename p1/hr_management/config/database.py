from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote_plus
db = SQLAlchemy()

def init_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"]=(
        "mysql+pymysql://root:Siddhi%4028062004%23@localhost/hr"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)