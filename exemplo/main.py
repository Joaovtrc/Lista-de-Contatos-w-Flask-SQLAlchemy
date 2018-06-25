from flask import Flask, render_template, request
from flask import jsonify

from DBClasses import Pessoa, Telefone,Endereco
from Database import getPessoas, insert, delete

app = Flask(__name__)

@app.route('/deletar',methods=['GET', 'POST'])
def deletar():
    if request.method == 'POST':
        nome = request.form['nome']
        retorno = delete(nome)
        if retorno:
            return render_template("listar.html", msg='Contato deletado')
        else :
            return render_template("listar.html", msg='Contato não encontrado')

    elif request.method == 'GET':
        return render_template("deletar.html")

@app.route('/listar')
def listar():
    return render_template("listar.html")

@app.route('/alterar',methods=['GET', 'POST'])
def alterar():
    if request.method == 'POST':
        nome=request.form['nome']
        return render_template("listar.html", nome=nome)
    elif request.method == 'GET':
        return render_template("alterar.html")

@app.route('/',methods=['GET', 'POST'])
def index():
    ps = getPessoas()
    return render_template("menu.html",my_list = ps)

@app.route('/cadastro',methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':

        p = Pessoa()
        t = Telefone()
        e = Endereco()

        nome = request.form['nome']
        email = request.form['email']
        telefone = request.form['telefone']
        endereco = request.form['endereco']
        numero = request.form['numero']
        cep = request.form['cep']

        p.nome = nome
        p.email = email


        t.numero = telefone

        e.rua = endereco
        e.numero = numero
        e.cep = cep
        p.telefones.append(t)
        p.enderecos.append(e)

        insert(t)
        insert(e)
        insert(p)

        return render_template("listar.html",nome=p.nome,email=p.email,telefone=telefone,endereco=endereco,numero=numero,cep=cep)

    elif request.method == 'GET':

        return render_template("cadastro.html")

@app.route('/users')
def return_users():
    users = getPessoas()
    return jsonify(users=users,len=len(users))

if __name__ == "__main__":

    app.run(port=1024,debug=True, use_reloader=True)