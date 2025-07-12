from flask import Blueprint, render_template, request, redirect, url_for, flash

main = Blueprint('main', __name__)

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
        print(f"Received message from {name} <{email}>: {message}")
        flash("Your message has been sent!", "success")
        return redirect(url_for('main.thanks'))
    return render_template('contact.html')

@main.route('/thanks')
def thanks():
    return render_template('thanks.html')
