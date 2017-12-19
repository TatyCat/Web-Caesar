from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

page_header = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
"""

form = """ 
        <form action="/rot" method="post">
            <label for="rot"> Rotate by: 
                <input type="text" id="rot" name="rot" value="0"/>
                <textarea name="text"></textarea>
            </label>     
           
            <input type="submit" value="Submit Query"/>
        </form>                            
      
      
      """

page_footer = """
    </body>
</html>
"""


@app.route("/rot", methods=['POST'])
def rotations():
    rotat = request.form['rot']
    text_box = request.form['text']
    rot_input = "<br>" +"<strong>" + rotat + "</strong>" + "<br>" + text_box
    content = page_header + rot_input + page_footer
    return content

@app.route("/")
def index():
    title = "<h1>Web Caesar</h1>"
    content = page_header + title + form + page_footer
    return content



app.run()