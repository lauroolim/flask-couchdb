from flask import Flask, render_template, request, redirect, url_for
from couchdb import Server
import os
app = Flask(__name__)

def get_db():
    try:
        couchdb_url = os.getenv('COUCHDB_URL', 'http://admin:root@localhost:5984/')
        couch = Server(couchdb_url)

        if 'notes_db' not in couch:
            db = couch.create('notes_db')
        else:
            db = couch['notes_db'] 
        return db   
    except Exception as e:
        print(f"erro ao conectar no banco: {e}")
        return None

@app.route("/", methods=["GET", "POST"])
def index():
    db = get_db()
    if db is None:
        return "erro ao conectar no banco", 500

    if request.method == "POST":
        title = request.form['title']
        content = request.form['content']
        note = {"title": title, "content": content}
        db.save(note)
        return redirect(url_for('index'))

    notes = db.view('_all_docs', include_docs=True)
    return render_template("index.html", notes=notes)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)