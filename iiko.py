from flask import Flask, request, render_template
import requests
from flask import Response
app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('my-form.html')


@app.route('/', methods=['POST'])
def my_form_post():

    text = request.form['text']
    port = request.form['port']
    processed_text = text.upper()
    tvalue = str(request.form['Type'])
    if request.form['action'] == 'Status':
        url = tvalue + "://" + text + ":" + port + "/resto/get_server_info.jsp?encoding=UTF-8"
        result = requests.get(url).content
        return Response(result, mimetype='text/xml')
    elif request.form['action'] == 'CRMID':
        url = tvalue + "://"    + text + ":" + port + "/resto/service/evoservices/testConnection.jsp"
        result = requests.get(url).content
        return Response(result)
    else:
        pass  # unknown

app.run(host='0.0.0.0', port=8080, debug=False)


