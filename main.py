from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    error = request.args.get("error")
    if error:
        error_esc = cgi.escape(error, quote=True)
        error_element = '<p class="error">' + error_esc + '</p>'
    else:
        error_element = ''

    # combine the pieces of html with jinja2
    main_content = error_element
    
    template = jinja_env.get_template('main_form.html')
    return template.render()



@app.route("/sign", methods=['POST'])
def signup():
    usernames = request.form['username']
    passwords = request.form['password']
    verifys = request.form['verifpass']
    emails = request.form['email']


    # TODO 1
    # The user leaves any of the following fields empty: username, password, verify password
    if usernames == "" or passwords == "" or verifys == "":
        error = "Please do not leave 'username', 'password' or 'verify password' empty"
        return redirect("/?error=" + error)

    # TODO 2
    # The user's username or password is not valid -- for example, 
    # it contains a space character 
    # or it consists of less than 3 characters 
    # or more than 20 characters 
    # (e.g., a username or password of "me" would be invalid).
    if " " in usernames or " " in passwords:
        error = "your username and/or password cannot contain space(s)"
        return redirect("/sign?error=" + error)

    if len(usernames) < 3 or len(usernames) > 20 or len(passwords) < 3 or len(passwords) > 20:    
        error = "your username and/or password cannot contain less than 3 or more than 20 characters"
        return redirect("/?error=" + error)

    # TODO 3
    # The user's password and password-confirmation do not match.
    if verifys !=  passwords:
        error = "Your verify password should be equal password"
        return redirect("/sign?error=" + error)
    
    # TODO 4
    #  The criteria for a valid email address in this assignment are that 
    # it has a single @, 
    # a single ., 
    # contains no spaces, 
    # and is between 3 and 20 characters long.
    if "@" not in emails or " " in emails or "." not in emails: 
        error = "Please enter a valid e-mail address"
        return redirect("/sign?error=" + error)

app.run()