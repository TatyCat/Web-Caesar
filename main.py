from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
            
        </style>
    </head>
    <body>
    
        <form action="/rot" method="post">
            <label for="rot"> Rotate by: 
                <input type="text" id="rot" name="rot" value="0"/>
                <textarea name="text"> {0} </textarea>
            </label>   
            <input type="submit" value="Submit Query"/>
        </form>    
                                
    </body>
</html>
"""

@app.route('/rot', methods=['POST'])
def encrypt():
    title = "<h1>Web Caesar</h1>"
    numb_rot = int(request.form['rot'])
    text_box = request.form['text']
    encryption = rotate_string(text_box, numb_rot)

    content = title + form.format(encryption)
    return content


@app.route('/', methods=['POST', 'GET'])
def index():
    title = "<h1>Web Caesar</h1>"
    content = title + form.format("")
    return content


app.run()
