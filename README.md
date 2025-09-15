# Quiz Game Web App

This project is a simple Quiz Game application built using Python and Flask. It fetches question data from an external API, manages quiz logic, and provides an interactive web interface for users to play the quiz in their browser.

https://github.com/user-attachments/assets/071a3ab9-df68-4771-b637-ab24d9b32b07

---

## Table of Contents
- [app.py](#apppy)
- [quiz_brain.py](#quiz_brainpy)
- [data.py](#datapy)
- [question_model.py](#questionmodelpy)
- [templates/](#templates)

---

## app.py

The `app.py` file is the main Flask application that handles routing, user interaction, and rendering web pages.

### Key Components:
- **Imports**: 
  - `get_question_data`: Fetches questions from the Open Trivia Database API.
  - `Question`: Handles individual questions.
  - `QuizBrain`: Manages the quiz logic.
  - `Flask` modules (`render_template`, `request`, `redirect`, `url_for`, `session`) to handle web requests and session data.

### Workflow:
1. **Homepage (`/`)**:
   - Fetches new questions from the API and converts them into `Question` objects.
   - Initializes a `QuizBrain` instance to manage the quiz.
   - Stores questions, score, and current question number in the session.
   - Renders `index.html` to start the quiz.

2. **Question Page (`/question`)**:
   - Displays the current question and tracks progress.
   - Handles user answers submitted via HTML forms.
   - Updates the score and moves to the next question.
   - Redirects to the result page after the last question.

3. **Result Page (`/result`)**:
   - Shows the user's final score.
   - Renders `result.html`.

---

## quiz_brain.py

The `quiz_brain.py` file contains the `QuizBrain` class, which manages the quiz's logic independently of Flask.

### Key Components:
- **Initialization (`__init__`)**:
  - Takes a list of questions (`question_list`) and initializes the question number and score.

- **still_has_questions()**:
  - Checks if there are any remaining questions.

- **next_question()**:
  - Retrieves the next question and increments the question number.

- **check_answer(user_answer, correct_answer)**:
  - Compares the user's answer with the correct answer (case-insensitive).
  - Updates the score if correct.

---

## data.py

The `data.py` file is used to fetch question data from the Open Trivia Database API.

### Key Components:
- **Parameters**:
  - `amount`: Specifies the number of quiz questions to fetch (10 in this case).
  - `type`: Sets the type of questions to "boolean" (True/False).

- **API Endpoint**:
  - The `api_endpoint` variable stores the URL for the Open Trivia Database API.

- **HTTP Request**:
  - `requests.get` sends an HTTP GET request to the API with the specified parameters.
  - `response.raise_for_status()` checks for HTTP errors.
  - Returns a list of questions to be used in the quiz.

---

## question_model.py

The `question_model.py` file contains the `Question` class, which is used to create question objects in the quiz.

### Key Components:
- **Initialization (`__init__`)**:
  - The `Question` class takes two arguments: `q_text` (the text of the question) and `q_answer` (the correct answer).
  - Stores them in `text` and `answer` attributes.

This class encapsulates quiz question data and makes it easier to manage and use within `QuizBrain` and the Flask app.

---

## templates/

The `templates/` folder contains the HTML files used to render the web pages.

### Key Pages:
- **index.html**: Homepage, displays the start button for the quiz.  
- **question.html**: Displays the current question, answer buttons, and progress.  
- **result.html**: Shows the final score after completing the quiz.

---

