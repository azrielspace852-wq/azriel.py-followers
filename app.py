from flask import Flask, render_template
from flask_cors import CORS
from config import Config
from routes import api_bp
import os

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

# Register blueprint
app.register_blueprint(api_bp)

@app.route('/')
def index():
    return render_template(
        'index.html',
        username=Config.TIKTOK_USERNAME,
        profile_name=Config.PROFILE_NAME,
        links=Config.LINKS,
        email=Config.EMAIL
    )

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=Config.PORT,
        debug=Config.DEBUG
    )