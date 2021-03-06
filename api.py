

from flask import Flask, render_template, request, redirect, flash, session, url_for

app = Flask(__name__)

app.secret_key = '5U\x9fa\xbb0w\xe3^*\xb2_\x02\x82H\rY\xcb\xc6\xa8.\xe7\xaa\xd8\x8f\xe4\xb70l0(\x12\xe259P\xef\xeb\xb7v\xecH\x08m,\x81\xd4\xf4'



@app.route("/")
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        
        print request.form
        print session

        if all(x in request.form for x in ('username','pw')): 
            
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        else:
            flash('something went wrong with your submission')
            return redirect(url_for('index'))

    elif request.method == 'GET':
        return redirect(url_for('index'))

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)