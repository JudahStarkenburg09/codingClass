from flask import Flask, render_template_string
import pyWebDev as PWD

app = Flask(__name__)

def clicked():
    print("Hello World")

@app.route('/')
def hello_world():
    html_content = ''
    html_content += PWD.text("Hello World", position=(200, 100))
    html_content += PWD.text("Hello World", position=(200, 200), underlined=True)
    html_content += PWD.button("Hello World", position=(200, 300), onclick="clicked()")
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=7824)
