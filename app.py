from pathlib import Path

from flask import Flask, render_template, jsonify
import calendar
from datetime import datetime

from services.news_script import generate_news_script
from services.speech import text_to_speech

app = Flask(__name__)

RESOURCE_DIR = Path(app.root_path) / "static" / "resource"
SUMMARY_MP3 = RESOURCE_DIR / "summary.mp3"

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
    依日期生成：文字雲(summary.png)、新聞稿、音檔(summary.mp3)、一句話摘要。
    新聞稿由 services.news_script 產生（GPT 隊友可替換實作）；
    音檔由 services.speech.text_to_speech 產生。
    """
    # TODO: 文字雲 → static/resource/summary.png（隊友負責）

    try:
        script = generate_news_script(year, month, day)
        text_to_speech(script, SUMMARY_MP3)
    except (FileNotFoundError, ValueError, RuntimeError) as exc:
        return jsonify({"error": str(exc)}), 500

    summary = script.split("。")[0] + "。" if "。" in script else script[:80]

    return jsonify({
        "summary": summary,
        "script": script,
    })


if __name__ == '__main__':
    app.run(debug=True)