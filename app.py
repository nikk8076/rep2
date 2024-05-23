from flask import Flask, render_template, request, redirect, url_for, flash,session,Response,send_file
app=Flask(__name__)
app.secret_key = '$$$$##)($'
db=dict()
@app.route("/login",methods=['POST','GET'])
def login():
    if request.method == 'POST':
        username=request.form['username']
        password=request.form['password']
        if username in db and db[username]==password:
            print("ok\n")
            return render_template('index.html',message="logged in")
        db[username]=password
        print("not ok\n")
        return render_template('index.html',message="signed up")

@app.route("/")
def start():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True,port=3000)