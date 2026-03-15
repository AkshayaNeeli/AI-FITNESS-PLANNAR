from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():

    if request.method=="POST":
        weight=float(request.form["weight"])
        height=float(request.form["height"])

        bmi=round(weight/(height*height),2)

        if bmi<18.5:
            category="Underweight"
        elif bmi<25:
            category="Normal Weight"
        elif bmi<30:
            category="Overweight"
        else:
            category="Obese"

        return render_template("result.html", bmi=bmi, category=category)

    return render_template("index.html")


@app.route("/tips")
def tips():
    return render_template("tips.html")


@app.route("/motivation")
def motivation():
    return render_template("motivation.html")


if __name__=="__main__":
    app.run(debug=True)