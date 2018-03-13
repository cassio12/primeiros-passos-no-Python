from flask import Flask 
app = Flask(__name__)

@app.route("/")
def hello():
	return 'Hello Word!!!'
@app.route("/receita")
def receita():
	return 'Receita'

if __name__ == '__main__':
	app.run()


# criar uma rota pra retornar uma receita 
	