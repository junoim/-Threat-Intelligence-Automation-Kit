from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'mytestkey123'  # Required for sessions

# SQLite Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///forum.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Silence the warning

db = SQLAlchemy(app)

# Database Model
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    content = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

# Dummy users
users = {
    "admin": "admin123",
    "user1": "test"
}

# Login Route
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        uname = request.form['username']
        pwd = request.form['password']
        if uname in users and users[uname] == pwd:
            session['username'] = uname
            return redirect('/forum')
        return "Invalid login!"
    return render_template('login.html')

# Forum Page
@app.route('/forum', methods=['GET', 'POST'])
def forum():
    if 'username' not in session:
        return redirect('/')

    if request.method == 'POST':
        new_post = Post(username=session['username'], content=request.form['content'])
        db.session.add(new_post)
        db.session.commit()
        return redirect('/forum')

    posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template('forum.html', posts=posts)

# Logout Route
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')

# Add Suspicious Test Posts
@app.route('/addtest')
def addtest():
    p1 = Post(username='anon123', content='Is anyone selling fake passports?')
    p2 = Post(username='hacker4hire', content='Download this malware now!')
    p3 = Post(username='techguy', content='How to install Linux on a VM?')
    p4 = Post(username='deepbuyer', content='Looking to buy guns, contact me via XMPP.')
    p5 = Post(username='cyberlord', content='Zero-day exploit for sale. Bitcoin only. My wallet is bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh.')
    db.session.add_all([p1, p2, p3, p4, p5])
    db.session.commit()
    return "Test posts added!"

# Initialize DB and Run
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
