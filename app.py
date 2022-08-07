from flask import Flask, render_template, request
import sqlite3
import json

app = Flask('__name__')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/')
def index():
    conn = sqlite3.connect('todo.db')
    todos = conn.execute("SELECT NAME, DESCRIPTION from TODOS").fetchall()
    conn.close()
    return render_template('index.html', todos=todos)


@app.route('/savetodo', methods=['POST'])
def savetodo():
    name = request.form.get('name')
    description = request.form.get('description')
    conn = sqlite3.connect('todo.db')
    conn.execute("INSERT INTO TODOS (NAME, DESCRIPTION) \
        VALUES (?, ?)",
                 (name, description))
    conn.commit()
    conn.close()
    return "success"


@app.route('/deletetodo', methods=['DELETE'])
def deletetodo(methods=['DELETE']):
    todoToDelete = request.form.get('todoToDelete')
    todoToDeleteFormatted = "'" + todoToDelete + "'"
    conn = sqlite3.connect('todo.db')
    conn.execute("DELETE from TODOS where NAME = ?;", [todoToDelete])
    conn.commit()
    conn.close()
    return "success"


if __name__ == '__main__':
    # ! Remove debug = True after development
    app.run(debug=True, host='0.0.0.0')
