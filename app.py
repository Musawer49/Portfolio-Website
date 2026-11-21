from flask import Flask, render_template

app = Flask(__name__)

# Fill in one dict per project. Leave demo_url as None until the demo exists.
PROJECTS = [
    {
        "slug": "project-one",
        "name": "Personal Expense Tracker",
        "tagline": "It tracks your personal expenses",
        "problem": "[What was slow, manual or error-prone before this existed]",
        "input": {"title": "[e.g. messy CSV files]", "note": "[Where the data comes from]"},
        "process": {"title": "[e.g. clean, validate, merge]", "note": "[The Python logic in one line]"},
        "output": {"title": "[e.g. one ready report]", "note": "[What the user gets]"},
        "stack": "[Python, libraries]",
        "time_saved": "[X hrs → Y sec]",
        "demo_label": "[Live, sample data]",
        "demo_url": None,
        "image": "expense-tracker.png",
        "image_alt": "Describe what the screenshot shows, e.g. the main window with the expense list and budget summary",
        "github_url": "https://github.com/Musawer49/[repo-name]",
    },
]


@app.route("/")
def index():
    return render_template("index.html", projects=PROJECTS)


if __name__ == "__main__":
    app.run(debug=True)