import os
from werkzeug.utils import secure_filename
from flask import Flask, request, render_template, jsonify, url_for
import util  # Ensure this module exists

application = Flask(__name__)

# Allowed file extensions for image uploads
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}

# Ensure the uploads folder exists
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Create folder if not exists
application.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Load the necessary model artifacts
try:
    util.load_artifacts()
except Exception as e:
    print(f"Error loading artifacts: {e}")

# Function to check if file type is allowed
def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

# Home page
@application.route("/")
def home():
    try:
        classifywaste_url = url_for("classifywaste")
    except Exception as e:
        classifywaste_url = "#"
        print("Error generating classifywaste_url:", str(e))  # Debugging

    return render_template("home.html", classifywaste_url=classifywaste_url)

# Classify waste
@application.route("/classifywaste", methods=["POST"])
def classifywaste():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    image_data = request.files["file"]

    if image_data.filename == "":
        return jsonify({"error": "No selected file"}), 400

    if not allowed_file(image_data.filename):
        return jsonify({"error": "Invalid file type. Only PNG, JPG, JPEG, and GIF allowed."}), 400

    # Save the image
    image_path = os.path.join(application.config["UPLOAD_FOLDER"], secure_filename(image_data.filename))
    image_data.save(image_path)

    try:
        # Classify waste using the model
        predicted_value, details, video1, video2 = util.classify_waste(image_path)
        os.remove(image_path)  # Cleanup uploaded file
    except Exception as e:
        return jsonify({"error": f"Error processing image: {str(e)}"}), 500

    return jsonify(predicted_value=predicted_value, details=details, video1=video1, video2=video2)

# Custom 404 error page
@application.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

if __name__ == "__main__":
    application.run(debug=True)
