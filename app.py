from flask import Flask, render_template, request, redirect
import csv, datetime

app = Flask(__name__)



@app.route("/")
def index():
    scores = readScores()
    print(scores[0])
    print(scores[1])
    return render_template('index.html', joneScores = scores[0], oyScores = scores[1])

@app.route("/writeKudo", methods=["POST"])
def writeKudo():
    name = request.form["name"]
    kudo = request.form["kudo"]
    if name and kudo:
        writeKudoToFile(name, kudo)
    return redirect("/")

def readScores():
    joneScores = {}
    oyScores = {}
    with open('kudos.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter="|")
        for row in reader:
            if ''.join(row).strip():
                if row[0] == "Jone":
                    joneScores[row[1]] = row[2]
                elif row[0] == "Øystein":
                    oyScores[row[1]] = row[2]
    return [joneScores, oyScores]

def writeKudoToFile(name, kudo):
    date = datetime.date.today()
    with open('kudos.csv', 'a') as csvfile:
        writer = csv.writer(csvfile, delimiter='|')
        writer.writerow([name, kudo, date])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8088)

