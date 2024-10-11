from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
tasks = []  

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)
 
@app.route('/process', methods=['POST'])
def process_form():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    task = request.form.get('task')
    if task:
        tasks.append(task)

    return render_template('second.html', name=name, email=email, message=message, tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True)
