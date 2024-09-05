from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Inicializando uma lista de tuplas para armazenar tarefas e descrições
tarefas_descricoes = []

@app.route('/', methods=["GET", "POST"])
def principal():
    if request.method == "POST":
        tarefa = request.form.get("tarefa")
        descricao = request.form.get("descricao")
        
        if tarefa and descricao:
            tarefas_descricoes.append((tarefa, descricao))
    
    # Passa uma lista de tuplas contendo índices e tarefas descrições
    tarefas_descricoes_with_index = list(enumerate(tarefas_descricoes))
    return render_template("index.html", tarefas_descricoes_with_index=tarefas_descricoes_with_index)

@app.route('/remover_tarefa/<int:index>', methods=["POST"])
def remover_tarefa(index):
    if 0 <= index < len(tarefas_descricoes):
        tarefas_descricoes.pop(index)
    return redirect(url_for('tarefa_removida'))

@app.route('/tarefa_removida')
def tarefa_removida():
    return render_template('tarefa_removida.html')

if __name__ == '__main__':
    app.run(debug=True)
