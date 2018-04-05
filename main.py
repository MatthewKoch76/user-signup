from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')

def index():
    return render_template('forms.html')

@app.route('/signup', methods=['POST'])

def checkform():
    
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']

    name_error = ''
    password_error = ''
    verify_password_error = ''
    email_error = ''
        
    if not len(username) in range(3,21):
        name_error = 'please enter a username between 3-20 characters without spaces'
    if ' ' in username:
        name_error = 'please enter a username between 3-20 characters without spaces'
    if not len(password) in range(3,21):
        password_error = 'please enter a password between 3-20 characters without spaces'
    if ' ' in password:
        password_error = 'please enter a password between 3-20 characters without spaces'
    if password != verify_password:
        verify_password_error = 'passwords must match' 
    if email != '':
        if '.' not in email:
            if '@' not in email:
                email_error = 'not a valid email'
    if name_error == '':
        if password_error == '':
            if verify_password_error =='':
                if email_error == '':
                    return render_template('welcome.html', username=username)
                else:
                    return render_template('forms.html', 
    username = username,
    password = password,
    verify_password = verify_password,
    email = email,
    name_error = name_error, 
    password_error = password_error, 
    verify_password_error = verify_password_error,
    email_error = email_error,)
            else:
                return render_template('forms.html', 
    username = username,
    password = password,
    verify_password = verify_password,
    email = email,
    name_error = name_error, 
    password_error = password_error, 
    verify_password_error = verify_password_error,
    email_error = email_error,)
        else:
            return render_template('forms.html', 
    username = username,
    password = password,
    verify_password = verify_password,
    email = email,
    name_error = name_error, 
    password_error = password_error, 
    verify_password_error = verify_password_error,
    email_error = email_error,)
    else:
        return render_template('forms.html', 
    username = username,
    password = password,
    verify_password = verify_password,
    email = email,
    name_error = name_error, 
    password_error = password_error, 
    verify_password_error = verify_password_error,
    email_error = email_error,)
        
app.run()

