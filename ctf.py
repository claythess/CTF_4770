from flask import Flask,  render_template, request, send_from_directory
import socket
app = Flask(__name__, static_folder="static")

answer = "Enter a expression and Click Submit"
calc_html = """
<html>
<font size="+20">%s</font>
<form>
    Expression:<br>
    <input type="text" name="answer"></br>
    <br><input type="submit" name="sub" value="Submit">
</form>
</html>
"""

@app.route('/')
def display():
    return """Welcome to my super duper cool website. I got some real cool stuff but pls dont hack me 👉👈. <br> Anyway good luck finding a list of pages anyway<br>
<IMG SRC="https://media.licdn.com/dms/image/v2/C5103AQEH3UyEgnL51A/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1516756298902?e=1739404800&v=beta&t=BxtJWlGjDzkrrb4sWHkvH650WbWyI49cu77lgfFlhiY">"""

@app.route('/robots.txt',methods=["GET"])
def robots():
    return send_from_directory(app.static_folder,"robots.txt")

@app.route('/calculator')
def calc():
    global answer
    c = request.args.get("answer")
    if c != None:
        try:
            print("Command issued: ",c)
            exec(f"answer = {c}",globals())
        except Exception as e:
            print("Error:",e.with_traceback(None))
            answer = "Error"
    return calc_html % answer

@app.route('/deathcult')
def deathcult():
    return '''<html>
<A HREF="https://www.deathcult.fun/">
<IMG SRC="https://www.deathcult.fun/idcflogo.png">
<br> Join The Cult </a></font></html>'''



@app.route('/myfavthings')
def things():
    return '''
<html>
Raindrops  on roses
<br>
wiskers on kittens
<br>
gumdrops and somethiong something something mittens
<br>
something and this or that and the other thing
<br>
these are a few of my favorite things.
</html>
'''

@app.route('/reflect')
def reflect():
    global answer
    c = request.args.get("answer")
    if c == None:
        c=""
    return """
<html>
<font size="+20">You Entered: %s</font>
<form>
    <br>
    <input type="text" name="answer"></br>
    <br><input type="submit" name="sub" value="Submit">
</form>
</html>
""" % c

@app.route('/grade')
def grade():
    return """<html><font size="+5000">Pls gimme an A</font></html>"""


if __name__=='__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8",80))
    ip = str(s.getsockname()[0])
    app.run(host=ip)