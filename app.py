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


@app.route("/api/summary/<int:year>/<int:month>/<int:day>")
def api_summary(year, month, day):
    r"""
    TODO:
    改成根據日期生成對應的文字雲、文字稿、文字稿音檔、文字稿摘要(一句話)
    文字雲要存到 nlp_final_project\static\resource\summary.png
    文字稿音檔存到 nlp_final_project\static\resource\summary.mp3
    並回傳文字稿摘要(一句話)給前端
    """
    import time
    time.sleep(3)  # 模擬生成摘要的時間

    summary = f"Summary for {year}-{month:02d}-{day:02d}: This is a sample summary of the day's events."

    return jsonify({
        "summary": summary
    })


if __name__ == '__main__':
    app.run(debug=True)