from flask import Flask, redirect, url_for, render_template, session
from flask_wtf import FlaskForm
from wtforms import StringField


class FilmeForm(FlaskForm):
    nome_filme = StringField('Título do filme')

app = Flask(__name__)
app.secret_key = 'oWall'
@app.route('/', methods=['GET','POST'])
def home():
    form = FilmeForm()
    
    if form.validate_on_submit():
        filme = form.nome_filme.data
        if 'filmes' not in session:
            session['filmes'] = []
        session['filmes'].append(filme)
        session['filmes'] = session['filmes']
        return render_template('index.html', form=form, filmes=session.get('filmes', []))

    return render_template('index.html', form=form, filmes=session.get('filmes', []))

#Rota para remover filmes
@app.route('/remover/<indice>', methods=['POST'])
def remover_filme(indice):
    if 'filmes' in session:
        del session['filmes'][int(indice)]
        session['filmes'] = session['filmes']
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)