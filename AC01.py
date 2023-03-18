from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def main():

    resultado = 'Bem-vindo! Por favor, entre as notas na URL usando os parâmetros "notaUm" e "notaDois".'
    
    notaUm = request.args.get('notaUm')
    notaDois = request.args.get('notaDois')

    if notaUm is not None and notaDois is not None:
        
        try:
            notaUm = float(notaUm)
            notaDois = float(notaDois)
            
            media = (notaUm + notaDois) / 2

            if media >= 7:
                resultado = 'Aprovado, sua média foi: ' + str(media)
            elif media >= 5 and media < 7:
                resultado = 'Você está de DP, sua média foi: ' + str(media)
            else:
                resultado = 'Reprovado, sua média foi: ' + str(media)
                
        except ValueError:
            resultado = 'Por favor, entre as notas como números válidos.'

    return resultado

if __name__ == '__main__':
    app.run(debug=True)