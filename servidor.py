from flask import Flask, request, jsonify
import time

# Initialize the Flask application
app = Flask(__name__)


@app.route('/', methods=['POST'])
def post():
    # Get the parsed contents of the form data
    json = request.json
    print time.strftime("%d/%m/%Y") + " - " + time.strftime("%H:%M:%S") + " | Para: " + json['remetente'] +\
          " - Mensagem: " + json['mensagem']
    destino = '/var/spool/sms/outgoing/%s.txt' % (json['remetente'])
    arquivo = open(destino, 'a')
    arquivo.write("To: %s \n\n%s" % (json['remetente'], json['mensagem']))
    arquivo.close()
    # Render template
    return jsonify(json)

# Run
if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=8000
    )
