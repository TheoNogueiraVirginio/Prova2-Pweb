from flask import session

def obter_filmes():
    return session.get('filmes', [])

def adicionar_filme(filme):
    if 'filmes' not in session:
        session['filmes'] = []
    session['filmes'].append(filme)
    session['filmes'] = session['filmes']

    return session['filmes']

def remover_filme(indice):
    if 'filmes' in session:
        del session['filmes'][int(indice)]
        session['filmes'] = session['filmes']
    return session['filmes']

def contar_filmes():
    return len(session.get('filmes', []))