from flask import Flask
from extensions import db
from routes import api
from auth import auth

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "your_secret_key"

db.init_app(app)

app.register_blueprint(api, url_prefix='/api')
app.register_blueprint(auth, url_prefix='/auth')

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
