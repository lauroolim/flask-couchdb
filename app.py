from flask import Flask, render_template, request, redirect, url_for
from couchdb import Server
from datetime import datetime
import os
import uuid
app = Flask(__name__)

def get_db():
    try:
        couch = Server(os.getenv('COUCHDB_URL', 'http://admin:root@localhost:5984/'))

        if 'notes_db' not in couch:
            db = couch.create('notes_db')
        else:
            db = couch['notes_db'] 
        return db   
    except Exception as e:
        print(f"erro ao conectar no banco: {e}")
        return None

def gen_id(prefix: str) -> str:
    return f"{prefix}:{uuid.uuid4().hex}"

@app.route("/", methods=["GET", "POST"])
def index():
    db = get_db()
    if db is None:
        return "erro ao conectar no banco", 500

    if request.method == "POST":
        kind = request.form.get('kind')
        if kind == 'tag':
            tag_doc = {
                "_id": gen_id("tag"),
                "type": "tag",
                "name": request.form['name'],
                "created_at": datetime.utcnow().isoformat()+"Z"
            }
            db.save(tag_doc)
        elif kind == 'user': 
            user_doc = {
                "_id": gen_id("user"),
                "type": "user",
                "name": request.form['name'],
                "email": request.form['email'],
                "created_at": datetime.utcnow().isoformat()+"Z"
            }
            db.save(user_doc)
        elif kind == 'note':
            note_doc = {
                "_id": gen_id("note"),
                "type": "note",
                "title": request.form['title'],
                "content": request.form['content'],
                "user_id": request.form['user_id'],
                "tag_id": request.form.get('tag_id'), 
                "created_at": datetime.utcnow().isoformat()+"Z"
            }
            db.save(note_doc)
        return redirect(url_for('index'))


    users = [r.doc for r in db.view('app/all_users', include_docs=True)]
    tags  = [r.doc for r in db.view('app/all_tags', include_docs=True)]
    notes = [r.doc for r in db.view('app/notes_by_user', include_docs=True)]

    return render_template("index.html", users=users, tags=tags, notes=notes)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)