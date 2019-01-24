from flask import Flask,render_template
app=Flask(__name__)

@app.route('/')
def index():
    #list1=['komal','aarti','harshita']
    dic={
        1:'komal',
        2:'aarti',
        3:'harshita'
        }
    print(dic)
    return render_template('tmp.html',result=dic)
   # return render_template('tmp.html',list1=list1,list=list1[1],dic=dic)
if __name__=='__main__':
    app.run(debug=True)
