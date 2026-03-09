from flask import Flask, request, redirect

app = Flask(__name__)

schedule = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        title = request.form["title"]
        time = request.form["time"]
        schedule.append(f"{time} - {title}")
        return redirect("/")

    page = """
    <h1>Wi-Fi Scheduling App</h1>
    <form method="POST">
        Event: <input name="title" required><br>
        Time: <input name="time" required><br>
        <button>Add Event</button>
    </form>
    <h2>Schedule</h2>
    <ul>
    """
    for event in schedule:
        page += f"<li>{event}</li>"
    page += "</ul>"

    return page

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)