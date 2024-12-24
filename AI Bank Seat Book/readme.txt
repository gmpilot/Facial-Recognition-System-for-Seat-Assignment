_____________ Facial Recognition System for Seat Assignment _____________

This project is a Flask-based web application that utilizes facial recognition to determine seat priority based on the user's age, gender, and emotion. The application assigns a seat based on a set of predefined rules and stores a history of recent seat assignments.

** Features:
- Check live image to analyze age, gender, and emotion.
- Determine seat priority based on age and gender.
- Save and display the seat assignment history.
- Interactive web interface built with Flask.

** Requirements:
Before running the application, ensure you have the following installed:
- Python 3.7 or later
- pip (Python package manager)

** Installation Instructions:
1. Clone this repository or download the project files to your local machine.

2. Navigate to the project directory and create a virtual environment (optional but recommended):
   - python -m venv venv


3. Activate the virtual environment:
   # On Windows:
     - venv\Scripts\activate

   # On macOS/Linux:
     - source venv/bin/activate

4. Install the required dependencies:
   - pip install -r requirements.txt


** Running the Application:
1. After installing the dependencies, run the Flask app:
   - python app.py

2. The app will start running locally at `http://127.0.0.1:5000/`.

3. Open a web browser and navigate to the above URL to use the application.
