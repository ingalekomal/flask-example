from flask import Flask
app=Flask(__name__)

#@app.route('/hi/<name>')
#def hello_name(name):
#    return 'Hello ' + name

#@app.route('/hi/<int:no>')
#def hello_num(no):
#    return 'No is %d! '%no

@app.route('/hi/<float:no>')
def hello_num(no):
    return 'No is %d! '%no

if __name__=="__main__":
    app.run(debug=True)
