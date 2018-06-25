from flask import Flask, render_template, request, redirect, url_for
from flask import jsonify

from DBClasses import Contato, Telefone,Endereco
from Database import insertEdit, deletarContato, getContatos, getSingleContato, deletarEndereco, deletarTelefone

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def listar():
    contatos = getContatos()
    return render_template("home.html",contatos = contatos)

@app.route('/cadastro',methods=['GET', 'POST'])
@app.route('/cadastro/<int:id>',methods=['GET', 'POST'])
def cadastrar(id=-1):
    c = Contato()
    t = Telefone()
    e = Endereco() 
    telefones = []
    telefones.append(t)

    if(id != -1):
        c = getSingleContato(id)

    else:
        c.telefones.append(t)
        c.enderecos.append(e)

    if request.method == 'POST':
        if(id != -1):
            print(request.form)
            c.nome = request.form['nome']
            c.email = request.form['email']
            print(c.telefones)
            for i in range(0, len(c.telefones), 1):
                print(c.telefones[i].telefone)
                c.telefones[i].telefone = request.form['telefone' + str(c.telefones[i].id)]
                c.telefones[i].tipo = request.form['tipo_tel' + str(c.telefones[i].id)]

            for i in range(0, len(c.enderecos), 1):
                c.enderecos[i].endereco = request.form['endereco' + str(c.enderecos[i].id)]
                c.enderecos[i].numero = request.form['numero' + str(c.enderecos[i].id)]
                c.enderecos[i].cep = request.form['cep' + str(c.enderecos[i].id)]

            print(c.telefones[0].telefone)
            insertEdit(c)

        else:
            print(request.form)
            c.nome = request.form['nome']
            c.email = request.form['email']
            t.telefone = request.form['telefone']
            e.endereco = request.form['endereco']
            e.numero = request.form['numero']
            e.cep = request.form['cep']

            c.telefones.append(t)
            c.enderecos.append(e)

            insertEdit(t)
            insertEdit(e)
            insertEdit(c)

        return redirect(url_for('listar'))

    elif request.method == 'GET':

        return render_template("cadastro.html", c=c, telefones=telefones)

@app.route('/delete/<int:id>', methods=['GET','POST'])
def delete(id):
    deletarContato(id)
    return redirect(url_for('listar'))

##TELEFONE
@app.route('/adicionartelefone/<int:id>', methods=['GET','POST'])
def addPhone(id):
    c = getSingleContato(id)
    t = Telefone()
    if request.method == 'POST':
        if(id != -1):
            t.telefone = request.form['telefone']
            t.tipo = request.form['tipo_tel']
            c.telefones.append(t)
            insertEdit(c)

        return redirect(url_for('listar'))
    return render_template("addphone.html", c=c)


@app.route('/deletartelefone/<int:id>', methods=['GET','POST'])
def deletePhone(id):
    deletarTelefone(id)
    return redirect(url_for('listar'))


##ENDERECO
@app.route('/adicionarendereco/<int:id>', methods=['GET','POST'])
def addAddress(id):
    c = getSingleContato(id)
    e = Endereco()
    if request.method == 'POST':
        if(id != -1):
            e.endereco = request.form['endereco']
            e.numero = request.form['numero']
            e.cep = request.form['cep']
            c.enderecos.append(e)
            insertEdit(c)
        return redirect(url_for('listar'))

    return render_template("addaddress.html", c=c)

@app.route('/deletarendereco/<int:id>', methods=['GET','POST'])
def deleteAddress(id):
    deletarEndereco(id)
    return redirect(url_for('listar'))
        

if __name__ == "__main__":
    app.run(debug=True)