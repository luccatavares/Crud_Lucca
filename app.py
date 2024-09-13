from flask import Flask, render_template, request, flash, redirect
app = Flask(__name__)
from database import db
from flask_migrate import Migrate
from models import Viagem
app.config['SECRET_KEY'] = '9ebe6f92407c97b3f989420e0e6bebcf9d1976b2e230acf9faf4783f5adffe1b'

conexao = "mysql+pymysql://alunos:cefetmg@127.0.0.1/Viagem" #quando for criar o banco de dados coloca viagem
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/viagem")
def viagem():
    u = Viagem.query.all()
    return render_template("viagem_lista.html", dados=u)

@app.route("/viagem/add")
def viagem_add():
    return render_template('viagem_add.html')

@app.route("/viagem/save", methods=['POST'])
def viagem_save():
    destino = request.form.get('destino')
    data_saida = request.form.get('data_saida')
    preco = request.form.get('preco')
    if destino and data_saida and preco:
        viagem = Viagem(destino, data_saida, preco)
        db.session.add(viagem)
        db.session.commit()
        flash('Viagem marcada com sucesso!!!')
        return redirect('/viagem')
    else:
        flash('Preencha todos os campos!!!')
        return redirect('/viagem/add')

@app.route("/viagem/remove/<int:id_pacote>")
def viagem_remove(id_pacote):
    viagem = Viagem.query.get(id_pacote)
    if viagem:
        db.session.delete(viagem)
        db.session.commit()
        flash("Viagem cancelada com sucesso!!")
        return redirect("/viagem")
    else:  
        flash("Caminho Incorreto")
        return redirect("/viagem")

@app.route("/viagem/edita/<int:id_pacote>")
def viagem_edita(id_pacote):
    viagem = Viagem.query.get(id_pacote)
    return render_template("viagem_edita.html", dados=id_pacote)

@app.route("/viagem/editasave", methods=["POST"])
def viagem_editasave():
    destino = request.form.get('destino')
    data_saida = request.form.get('data_saida')
    preco = request.form.get('preco')
    id_pacote = request.form.get('id_pacote')
    if id_pacote and destino and data_saida and preco:
        viagem = Viagem.query.get('id_pacote')
        viagem.id_pacote = id_pacote
        viagem.destino = destino
        viagem.data_saida = data_saida
        viagem.preco = preco
        db.session.commit()
        flash("Viagem atualizada com sucesso!")
        return redirect("/viagem")
    else:
        flash("Faltando dados!!!")
        return redirect("/viagem")


if __name__ == '_main_':
    app.run()