from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def signup_form():
    template = jinja_env.get_template('main_form.html')
    return template.render(username='', username_error='', 
    password='', password_error='',
    verifpass='', verifpass_error='', 
    email='', email_error='')

@app.route("/", methods=['POST'])
def signup():
    usernames = request.form['username']
    passwords = request.form['password']
    verifys = request.form['verifpass']
    emails = request.form['email']

    username_error = '' 
    password_error = ''
    verifpass_error = '' 
    email_error = ''
    
    if usernames == "":
        username_error = "Please do not leave 'username' empty"
    
    if len(usernames) < 3 or len(usernames) > 20:
        username_error = "'Username' cannot contain less than 3 or more than 20 characters"  
                    
    if " " in usernames:
        username_error = "'Username' cannot contain space(s)"

    if passwords == "":
        password_error = "Please do not leave 'password' empty"

    if " " in passwords:
        password_error = "'Password' cannot contain space(s)"
    
    if verifys == "":
        verifpass_error = "Please do not leave 'verify password' empty"

    if verifys !=  passwords:
        verifpass_error = "'Verify password' should be equal 'password'"
    
    if emails == "":
        email_error = "Please do not leave 'email' empty"

    if "@" not in emails or "." not in emails: 
        email_error = "Please enter a valid e-mail address"

    if not username_error and not password_error and not verifpass_error and not email_error:
        template = jinja_env.get_template('sucess_form.html')
        return template.render(usernames=usernames, 
                                passwords=passwords, 
                                verifys=verifys,
                                emails=emails)
    
    else:
        template = jinja_env.get_template('main_form.html')
        return template.render(username_error=username_error, 
                                password_error=password_error,
                                verifpass_error=verifpass_error, 
                                email_error=email_error, 
                                usernames=usernames, 
                                passwords=passwords, 
                                verifys=verifys,
                                emails=emails)



app.run()