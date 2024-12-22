from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'
DATABASE = 'database.db'

# Fungsi untuk koneksi database
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Route untuk halaman utama
@app.route('/')
def home():
    conn = get_db_connection()
    blogs = conn.execute('SELECT * FROM blogs').fetchall()
    conn.close()
    return render_template('index.html', blogs=blogs)

# Route untuk login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == 'admin' and password == '@12345678##':
            session['user'] = username
            return redirect(url_for('admin'))
        else:
            return "Invalid credentials. Please try again.", 401

    return render_template('login.html')

# Route untuk logout
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))

# Route untuk admin panel
@app.route('/admin')
def admin():
    if 'user' not in session:
        return redirect(url_for('login'))

    conn = get_db_connection()
    blogs = conn.execute('SELECT * FROM blogs').fetchall()
    conn.close()
    return render_template('admin.html', blogs=blogs)

# Route untuk menambah blog
@app.route('/add', methods=['GET', 'POST'])
def add_blog():
    if 'user' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title or not content:
            return "Title and content cannot be empty.", 400

        conn = get_db_connection()
        conn.execute('INSERT INTO blogs (title, content) VALUES (?, ?)', (title, content))
        conn.commit()
        conn.close()
        return redirect(url_for('admin'))

    return render_template('manage.html', action="Add")

# Route untuk menghapus blog
@app.route('/delete/<int:id>')
def delete_blog(id):
    if 'user' not in session:
        return redirect(url_for('login'))

    conn = get_db_connection()
    conn.execute('DELETE FROM blogs WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('admin'))

# Route untuk menampilkan blog penuh
@app.route('/blog/<int:id>')
def show_blog(id):
    conn = get_db_connection()
    blog = conn.execute('SELECT * FROM blogs WHERE id = ?', (id,)).fetchone()
    conn.close()

    if not blog:
        return "Blog not found", 404

    return render_template('blog_detail.html', blog=blog)

# Menjalankan aplikasi dengan host 0.0.0.0 dan port 5001
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
