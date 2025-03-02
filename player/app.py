from flask import Flask, render_template, jsonify, send_from_directory
import os

app = Flask(__name__)

DOWNLOADS_FOLDER = "downloads"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/list_audio")
def list_audio():
    """Returns a list of audio files in the downloads folder."""
    try:
        if not os.path.exists(DOWNLOADS_FOLDER):
            return jsonify([])  # If folder doesn't exist, return an empty list

        # Fix indentation: this should run regardless of whether the folder exists or not
        files = [f for f in os.listdir(DOWNLOADS_FOLDER) if f.endswith((".webm", ".mp3"))]

        print(files)
        return jsonify(files)
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route("/play_audio/<filename>")
def play_audio(filename):
    """Serves the requested audio file."""
    return send_from_directory(DOWNLOADS_FOLDER, filename)

if __name__ == "__main__":
    app.run(debug=True)
