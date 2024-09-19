# who-am-I/
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   ├── static/
│   │   ├── style.css
│   └── templates/
│       ├── base.html
│       ├── index.html
│       ├── quiz.html
│       ├── result.html
│
├── quiz.db
├── config.py
├── run.py
└── requirements.txt
Database Setup
To create the database and populate it with questions and answers, run the following commands in Python (Flask shell):

python
Copy code
from app import db
from app.models import Question, Answer

db.create_all()

# Create questions
q1 = Question(text="You enjoy large social gatherings.")
q2 = Question(text="You prefer to plan things rather than act spontaneously.")

db.session.add(q1)
db.session.add(q2)
db.session.commit()

# Create answers
a1_1 = Answer(text="Yes", personality_type="extrovert", question_id=q1.id)
a1_2 = Answer(text="No", personality_type="introvert", question_id=q1.id)
a2_1 = Answer(text="Yes", personality_type="analytical", question_id=q2.id)
a2_2 = Answer(text="No", personality_type="spontaneous", question_id=q2.id)

db.session.add_all([a1_1, a1_2, a2_1, a2_2])
db.session.commit()
4. Running the Application
Install dependencies:

pip install -r requirements.txt

Run the application:

python run.py
Open the application in your browser at http://localhost:5000/.
