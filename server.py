from flask import Flask, render_template, request, redirect 
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/button', methods = ['POST'])
# def display(count):
#     count = 0
#     return redirect('/')

if __name__=="__main__":
    app.run(debug=True)