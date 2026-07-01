from flask import Flask, redirect, url_for, render_template, session
from flask_wtf import FlaskForm
from wtforms import StringField

from app.functions import obter_filmes, adicionar_filme, remover_filme, contar_filmes

class FilmeForm(FlaskForm):
    nome_filme = StringField('Título do filme')

app = Flask(__name__)
app.secret_key = 'oWall'
@app.route('/', methods=['GET','POST'])
def home():
    form = FilmeForm()
    
    if form.validate_on_submit():
        filme = form.nome_filme.data
        adicionar_filme(filme)
        return redirect(url_for('sucesso'))

    return render_template('index.html', form=form, filmes=obter_filmes(), qtd_filmes=contar_filmes())

@app.route('/sucesso')
def sucesso():
    return render_template('sucesso.html', filmes=obter_filmes(), qtd_filmes=contar_filmes())

@app.route('/remover/<indice>', methods=['POST'])
def remover_filme_route(indice):
    remover_filme(indice)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)