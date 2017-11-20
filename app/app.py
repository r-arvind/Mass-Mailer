from flask import Flask,render_template,request
from mail import mail
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        toemail = request.form['toemail']
        subject = request.form['subject']
        content = request.form['content']
        mail(toemail,subject,content)
        return render_template('final.html')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    
    
    
