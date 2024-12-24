from flask import Flask, render_template, request, jsonify
from deepface import DeepFace
import random
from PIL import Image

app = Flask(__name__)
seat_history = []


@app.route("/")
def home():
    return render_template("index.html", seat_history=seat_history)


@app.route("/analyze_face", methods=["POST"])
def analyze_face():
    try:
        file = request.files["image"]
        img = (
            Image.open(file.stream)
            .convert("RGB")
            .resize((224, 224), Image.Resampling.LANCZOS)
        )
        img.save("temp_frame.jpg")

        analysis = DeepFace.analyze(
            img_path="temp_frame.jpg",
            actions=["age", "gender", "emotion"],
            enforce_detection=True,
        )
        if isinstance(analysis, list):
            analysis = analysis[0]

        age = analysis.get("age", "Unknown")
        gender = analysis.get("dominant_gender", "Unknown").lower()
        emotion = analysis.get("dominant_emotion", "Neutral")

        priority, seat_number = determine_priority(age, gender)
        seat_history.append(
            {
                "seat_number": seat_number,
                "priority": priority,
                "age": age,
                "gender": gender,
                "emotion": emotion,
            }
        )

        if len(seat_history) > 5:
            seat_history.pop(0)

        return jsonify(
            {
                "age": age,
                "gender": gender,
                "emotion": emotion,
                "priority": priority,
                "seat_number": seat_number,
                "seat_history": seat_history,
            }
        )
    except Exception as e:
        return jsonify({"error": str(e)})


def determine_priority(age, gender):
    gender = gender.lower() if isinstance(gender, str) else "unknown"
    try:
        age = int(age) if age != "Unknown" else -1
    except ValueError:
        age = -1

    if 0 < age < 18:
        priority = 2 if gender == "female" else 3
    elif age >= 60 or (gender == "female" and age >= 50):
        priority = 1
    elif gender == "female" or (gender == "male" and 50 <= age < 60):
        priority = 2
    else:
        priority = 3

    seat_number = f"{'A' if priority == 1 else 'B' if priority == 2 else 'C'}{random.randint(1000, 9999)}"
    return priority, seat_number


if __name__ == "__main__":
    app.run(debug=True)