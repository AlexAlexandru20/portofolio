from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from flask_mail import Message
from . import mail
from threading import Thread

main = Blueprint('main', __name__)

def sendMailAsync(msg, app):
    with app.app_context():
        mail.send(msg)

def sendMailMyself(app, name, email, project_type, message):
    body = f"""
    New message from your portfolio contact form:

    Name: {name}
    Email: {email}
    Project Type: {project_type}
    Message:
    {message}
    """

    msg = Message(subject="New Contact Form Message",
                  body=body,
                  recipients=['dev@digitalcyber.digital'])
    
    try:
        Thread(target=sendMailAsync, args=(msg, app)).start()
    except Exception as e:
        print("Mail send error:", e)
        flash("Failed to send message. Please try again later.", "error")


def sendMailClient(app, name, email):
    body = f"Thank you {name},  for your interest! We'll be in touch!"

    msg = Message(subject="New Contact Form Message",
                  body=body,
                  recipients=[email])
    
    try:
        Thread(target=sendMailAsync, args=(msg, app)).start()
    except Exception as e:
        print("Mail send error:", e)
        flash("Failed to send message. Please try again later.", "error")

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        project_type = request.form.get('project-type')
        message = request.form.get('message')

        try:
            sendMailMyself(current_app._get_current_object(), name, email, project_type, message)
            sendMailClient(current_app._get_current_object(), name, email)
            flash('Message was sent succesfully. We\'ll be in touch', 'success')
            return redirect(url_for('main.index'))
        except Exception as e:
            print('Error: ', e)
            flash('Error. Please try again later', 'error')
    return render_template('contact.html')