from flask import Flask, render_template, jsonify, send_from_directory
import os

app = Flask(__name__)

# Update the downloads folder path to point to the cloned repository
DOWNLOADS_FOLDER = os.path.join(os.getcwd(), "YT_PREMIUM", "downloads")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/list_audio")
def list_audio():
    """Returns a list of audio files in the downloads folder."""
    try:
        if not os.path.exists(DOWNLOADS_FOLDER):
            return jsonify([])  # If folder doesn't exist, return an empty list

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
