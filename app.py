from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "skillforge_secret_key_2026"

# Mock Database for Hackathon
users_db = {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        session['user'] = email
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    return render_template('forgot_password.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/languages')
def languages():
    return render_template('languages.html')

@app.route('/assessment', methods=['GET', 'POST'])
def assessment():
    status = request.args.get('status', 'test') # 'test' or 'completed'
    return render_template('assessment.html', status=status)

@app.route('/tasks')
def tasks():
    payment_status = request.args.get('payment', 'pending') # 'pending' or 'completed'
    return render_template('tasks.html', payment_status=payment_status)

@app.route('/passport')
def passport():
    return render_template('passport.html')

@app.route('/hiring')
def hiring():
    return render_template('hiring.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)