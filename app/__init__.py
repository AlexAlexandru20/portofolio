from flask import Flask
from flask_mail import Mail

mail = Mail()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '1234567890'

    app.config['MAIL_SERVER'] = 'mail.privateemail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USE_SSL'] = True
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USERNAME'] = 'contact@digitalcyber.digital'     # your email here
    app.config['MAIL_PASSWORD'] = 'DigitalCyber25'      # app password or actual password
    app.config['MAIL_DEFAULT_SENDER'] = ('Digital Cyber', 'contact@digitalcyber.digital')

    mail.init_app(app)
    from .routes import main
    app.register_blueprint(main)

    return app
