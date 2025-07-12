from flask import Flask
from flask_mail import Mail

mail = Mail()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '1234567890'

    # Configure your mail server (example for Gmail SMTP)
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = 'alexpopwebdev@gmail.com'     # your email here
    app.config['MAIL_PASSWORD'] = 'auuwelitggfavorf'      # app password or actual password
    app.config['MAIL_DEFAULT_SENDER'] = ('Alexandru Popica', 'alexpopwebdev@gmail.com')

    mail.init_app(app)
    from .routes import main
    app.register_blueprint(main)

    return app
