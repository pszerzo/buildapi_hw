from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

df = pd.read_csv("dictionary.csv", sep=",")

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<word>")
def api(word):
    defi = df.loc[df["word"] == word]["definition"].squeeze()
    result_dict = {"definition": defi, "your word": word}
    return result_dict


if __name__ == "__main__":
    app.run(debug=True)