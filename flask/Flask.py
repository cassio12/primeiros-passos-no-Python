from flask import Flask 
app = Flask(__name__)

@app.route("/hello")
def hello():
	return "Hello Word !!!"

@app.route("/receitas")
def receita():
	return 'Receita de bolinho de chuva:<br>- 1 ovo <br>- 1 xícara (chá) de açúcar refinado<br>- 1 xícara (chá) de leite<br>- 1 colher (sopa) de fermento em pó<br>- farinha de trigo até dar ponto para fritar (colheradas)<br>- óleo para fritar'	
@app.route("/")
def erro():
	return 'Erro 404, Se vc for o bom são mesmo digite /nome na URL e o seu nome vai aparacer na tela do seu navegador', 404 
@app.route("/<nome>")
def nome(nome):
	return 'Cassio Luis é o bom são', 200

if __name__ == "__main__":
	app.run()


# criar uma rota pra retornar varias receita diferentes.
# criar uma rota para retornar uma receita especifica .
	