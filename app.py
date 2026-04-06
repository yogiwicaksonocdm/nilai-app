from flask import Flask, render_template, request, redirect
from models import db, Siswa

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    data = Siswa.query.all()
    return render_template('index.html', data=data)

@app.route('/tambah', methods=['GET', 'POST'])
def tambah():
    if request.method == 'POST':
        nama = request.form['nama']
        mapel = request.form['mapel']
        nilai = request.form['nilai']

        siswa = Siswa(nama=nama, mapel=mapel, nilai=nilai)
        db.session.add(siswa)
        db.session.commit()

        return redirect('/')
    return render_template('tambah.html')

@app.route('/hapus/<int:id>')
def hapus(id):
    siswa = Siswa.query.get(id)
    db.session.delete(siswa)
    db.session.commit()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
