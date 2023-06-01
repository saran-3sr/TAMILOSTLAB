from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    def __repr__(self):
        return f'<Student {self.firstname}>'
@app.route('/')
def home():
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)