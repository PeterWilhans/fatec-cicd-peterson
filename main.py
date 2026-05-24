import sqlite3
from flask import Flask, request

app = Flask(_name_)

@app.route('/user/<username>')
def buscar_usuario_vulneravel(username):
    """SQL Injection vulnerability - user input directly in query"""
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    query = f"SELECT * FROM usuarios WHERE username = '{username}'"
    cursor.execute(query)
    
    results = cursor.fetchall()
    conn.close()
    return str(results)

@app.route('/delete')
def deletar_usuario_vulneravel():
    """SQL Injection via query parameter"""
    user_id = request.args.get('id')
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    query = "DELETE FROM usuarios WHERE id = " + user_id
    cursor.execute(query)
    conn.commit()
    conn.close()
    return "Deleted"

@app.route('/update', methods=['POST'])
def atualizar_email_vulneravel():
    """SQL Injection via POST body"""
    email = request.form.get('email')
    user_id = request.form.get('id')
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    query = "UPDATE usuarios SET email = '%s' WHERE id = %s" % (email, user_id)
    cursor.execute(query)
    conn.commit()
    conn.close()
    return "Updated"

@app.route('/search', methods=['POST'])
def buscar_por_email():
    """SQL Injection via JSON body"""
    data = request.get_json()
    email = data.get('email')
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    query = "SELECT * FROM usuarios WHERE email = '{}'".format(email)
    cursor.execute(query)
    
    results = cursor.fetchall()
    conn.close()
    return str(results)

if _name_ == '_main_':
    app.run(debug=True)