from flask import Flask

app = Flask("microblog")


#aqui vai comentário. A funcao do @ é um decorator
@app.route("/")
def index():
    return "Hello Word"

app.run()