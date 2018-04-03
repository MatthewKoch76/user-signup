from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')

def index():
    return render_template('forms.html')

@app.route('/', methods=['POST'])

def sindex():
    username = request.form['Username']
    password = request.form['Password']
    verify_password = request.form['Verify_Password']
    email = request.form['Email']

    name_error = ''
    password_error = ''
    verify_password_error = ''
    email_error = ''
    
        
    if not len(username) in range(3,20):
        name_error = 'please enter a username between 3-20 characters'

    if password != verify_password:
        verify_password_error = 'passwords must match'

    

    return render_template('forms.html', 
    Username=username,
    Password = password,
    Verify_Password = verify_password,
    Email = email,
    name_error=name_error, 
    password_error=password_error, 
    verify_password_error=verify_password_error,
    email_error=email_error,)
        
app.run()

