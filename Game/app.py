from flask import Flask, render_template, request
import random 

app = Flask(__name__)

number = random.randint(1,100)
total = 0 

@app.route("/", methods=["GET", "POST"])
def home():
    global total,number,message,guess
    message =""

    if request.method =="POST":
        if "restart" in request.form:
            number=random.randint(1,100)
            total=0
            message="Game Restarted"
        else:
            guess= int(request.form["guess"])
            total +=1
        
            if guess == number:
                message = f"correct ! Attempts: {total}"
                total=0
            elif guess < number:
                message = "InCorrect! \nUp"
            else:
                message = "InCorrect! \ndown"
    return render_template("index.html", message=message)

if __name__=="__main__":
    # app.run(debug=True)
    app.run(host="0.0.0.0", port=5000)