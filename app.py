from flask import Flask, render_template, jsonify
import calendar
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/calendar/<int:year>/<int:month>")
def api_calendar(year, month):

    cal = calendar.Calendar(firstweekday=6)
    cal_data = cal.monthdayscalendar(year, month)

    return jsonify({
        "year": year,
        "month": month,
        "cal_data": cal_data
    })


if __name__ == '__main__':
    app.run(debug=True)