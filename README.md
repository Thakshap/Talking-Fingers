# Talking-Fingers

# A Multilingual Speech-to-Indian Sign Language Translator

Talking Fingers is a web-based application designed to bridge the communication gap between the hearing and deaf communities. It converts spoken or typed text in multiple Indian languages into Indian Sign Language (ISL) animations, making communication more inclusive and accessible.

---

## 🚀 Features

- **Multilingual Support**: Recognizes and translates Kannada, Hindi, Tamil, Telugu, and English.
- **Speech-to-Text Conversion**: Real-time transcription using the Web Speech API.
- **Text Translation**: Translates regional languages to English using `googletrans`.
- **NLP Processing**: Processes text using NLTK to tokenize, lemmatize, and clean input.
- **ISL Animations**: Maps processed text to ISL animations created in Blender 3D.
- **Responsive Interface**: User-friendly frontend built with HTML, CSS, and JavaScript.
- **Fallback Mechanism**: Handles unmapped words by breaking them into characters for ISL representation.

---

## 🛠️ Tech Stack

- **Backend**: Django
- **Speech Recognition**: Web Speech API
- **Translation**: `googletrans` Python library (`pip install googletrans==4.0.0-rc1`)
- **Natural Language Processing**: NLTK
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite
- **Animations**: Blender 3D (MP4 video format)

---

## 🔧 Installation and Setup

Follow these steps to set up the project on your local system:

1. **Clone the Repository**:
   git clone https://github.com/snehaballari/Talking-Fingers.git
   and move to the project directory
   - cd Talking-Fingers

2. Set Up a Virtual Environment: Create a virtual environment to isolate project dependencies:
   python -m venv venv

3. Activate the virtual environment:

   On Windows:
   venv\Scripts\activate

   On macOS/Linux:
   source venv/bin/activate

4. Install Project Dependencies: Install all required Python libraries:
   pip install -r requirements.txt

5. Apply Migrations: Set up the database and apply migrations:
   python manage.py migrate

6. Run the Development Server: Start the Django development server:
   python manage.py runserver

7. Access the Application: Open your web browser and navigate to:
   http://127.0.0.1:8000
