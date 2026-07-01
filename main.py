from flask import Flask, FlaskForm, redirect, url_for, render_template, session, StringField


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
        return redirect(url_for('home'))

    return render_template('index.html', form=form, filmes=session.get('filmes', []))

if __name__ == '__main__':
    app.run(debug=True)