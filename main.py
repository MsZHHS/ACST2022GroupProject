from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return '<a href="/factorRaw/100"> click here for an example</a>'

@app.route("/about", methods=["GET", "POST"])
def about():
    if request.method == "GET":
        return render_template("about.html")
    else:
        return calculate()

@app.route("/finalsgradecalc", methods=["GET", "POST"])
def finalsgradecalc():
    if request.method == "GET":
        return render_template("finalsgradecalc.html")
    else:
        return calcGrade()

def calcGrade():
    currGrade = float(request.form.get("currGrade"))
    desGrade = float(request.form.get("desGrade"))
    calculation = (desGrade - 0.8*currGrade) / 0.2
    return render_template("finalsgradecalc.html", currGrade=currGrade, desGrade=desGrade, calculation=calculation)

def calculate():
    category = request.form.get("category")
    raw_question = request.form.get("code")
    sample = category + raw_question
    return render_template("about.html", sample=sample, category=category, raw_question=raw_question)

@app.route('/Welcome/<name>')
def Welcome_name(name):
    return 'Welcome ' + name


def factors(num):
    return [x for x in range(1, num + 1) if num % x == 0]

@app.route('/factorRaw/<int:n>')
def factors_display_raw_html(n):
    list_factor = factors(int(n))
    html = "<h1> Factors of " + str(n) + " are</h1>" + "\n" + "<ul>"
    for f in list_factor:
        html += "<li>" + str(f) + "</li>" + "\n"
    html += "</ul> </body>"
    return html
    

if __name__ == "__main__":
    app.run(debug=True)