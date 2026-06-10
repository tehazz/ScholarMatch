# ScholarMatch — Scholarship Recommendation System

ScholarMatch is a Final Year Project developed to help students identify suitable scholarship options based on their academic and personal information. The system uses a Machine Learning approach to recommend scholarships such as MARA, PTPTN, and JPA based on selected student criteria.

The main goal of this project is to support students in making better scholarship application decisions by providing a simple, structured, and user-friendly recommendation system.

---

## Project Overview

Many students face difficulties in finding scholarships that match their academic background, financial condition, programme of study, and co-curricular involvement. Scholarship information is often scattered across different platforms, making it time-consuming for students to compare available opportunities.

ScholarMatch aims to solve this problem by providing a web-based recommendation system where students can enter their details and receive a suggested scholarship option. The system collects basic student information such as CGPA, family income, co-curricular score, programme of study, and year of study. These inputs are processed by a Machine Learning model to predict a suitable scholarship category.

This project is developed as a Flask-based web application, where the main system runs through `app.py`. The HTML pages are stored inside the `templates/` folder, while images, CSS files, and other static assets are stored inside the `static/` folder.

---

## Project Objectives

The objectives of this project are:

* To develop a web-based scholarship recommendation system.
* To recommend suitable scholarships based on student information.
* To apply a Machine Learning model for scholarship prediction.
* To provide information pages for selected scholarships such as MARA, PTPTN, and JPA.
* To create a simple and easy-to-use interface for students.
* To demonstrate how student-related data can be used to support scholarship recommendation.

---

## Scholarships Included

This system focuses on three scholarship or financial aid options:

### MARA

MARA provides financial assistance and education support, especially for eligible students in specific fields and income groups. In this system, MARA is included as one of the scholarship recommendation categories.

### PTPTN

PTPTN is a student education financing scheme that supports students pursuing higher education in Malaysia. It is included as one of the available financial aid options in the system.

### JPA

JPA provides sponsorship opportunities for eligible students based on academic performance and other requirements. In ScholarMatch, JPA is also included as one of the possible recommendation outputs.

---

## System Features

The system includes the following features:

* Homepage introducing the ScholarMatch system.
* Scholarship information pages for MARA, PTPTN, and JPA.
* ScholarMatch Finder page for student input.
* Machine Learning-based recommendation output.
* Simple and user-friendly website interface.
* Flask backend for routing, processing input, and displaying results.
* Static image support using the `static/` folder.
* HTML templates rendered through Flask using the `templates/` folder.

---

## Machine Learning Model

This project uses a **Decision Tree Classifier** as the Machine Learning model.

The model is trained using student-related attributes such as:

* CGPA
* Family income
* Co-curricular score
* Programme of study
* Year of study

The trained model predicts the most suitable scholarship category based on the input provided by the student.

Decision Tree Classifier is used because it is simple to understand, suitable for classification problems, and able to make predictions based on different decision conditions. This makes it appropriate for an academic prototype system such as ScholarMatch.

---

## Project Structure

The project does not use a separate frontend and backend folder. Instead, it follows a Flask project structure.

```text
ScholarMatch/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│   ├── index.html
│   ├── mara.html
│   ├── ptptn.html
│   ├── jpa.html
│   ├── recommendation.html
│   └── scholar.html
│
└── static/
    ├── style.css
    ├── mara.png
    ├── ptptn.png
    ├── jpa.png
    ├── logo.png
    └── script.js
```

---

## File and Folder Explanation

### `app.py`

The `app.py` file is the main file of the system. It runs the Flask application and connects all parts of the project together.

This file is responsible for:

* Starting the Flask web application.
* Creating routes for each page.
* Rendering HTML files from the `templates/` folder.
* Receiving student input from the recommendation form.
* Processing the input data.
* Running the Machine Learning prediction.
* Displaying the recommendation result to the user.

Example Flask route:

```python
@app.route("/")
def home():
    return render_template("index.html")
```

---

### `templates/`

The `templates/` folder contains all HTML files used in the system. Flask uses this folder to display the web pages.

Examples of files inside this folder include:

```text
index.html
mara.html
ptptn.html
jpa.html
recommendation.html
scholar.html
```

Each file has a specific purpose:

| File                  | Description                                           |
| --------------------- | ----------------------------------------------------- |
| `index.html`          | Homepage of the ScholarMatch system                   |
| `mara.html`           | Information page for MARA                             |
| `ptptn.html`          | Information page for PTPTN                            |
| `jpa.html`            | Information page for JPA                              |
| `recommendation.html` | Form page where users enter their details             |
| `scholar.html`        | Page that displays all scholarhips available in IIUM  |

---

### `static/`

The `static/` folder contains files that are not dynamically generated by Flask. These files are used for the design and visual elements of the website.

Examples of static files include:

* CSS files
* PNG images
* Icons
* Background images
* Other website assets

Example structure:

```text
static/
├── style.css
├── mara.png
├── ptptn.png
└── jpa.png
```

To use an image from the `static/` folder in an HTML file, Flask’s `url_for()` function can be used:

```html
<img src="{{ url_for('static', filename='mara.png') }}" alt="MARA">
```

To link a CSS file:

```html
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
```

---

### `requirements.txt`

The `requirements.txt` file lists the Python libraries needed to run the project.

Example:

```text
Flask
pandas
numpy
scikit-learn
```

This file makes it easier for other users to install the required libraries using:

```bash
pip install -r requirements.txt
```

---

## Dataset Notice

The dataset used for training and testing is **not included** in this repository.

The dataset has been removed to protect participant privacy and avoid exposing sensitive student-related information. The original dataset may contain details such as:

- CGPA
- Family income
- Programme of study
- Year of study
- Co-curricular score
- Scholarship recommendation category

Because this information is related to student profiles, it should not be publicly uploaded to GitHub.

This repository only contains the source code and system files needed to demonstrate the structure and implementation of the ScholarMatch project.

Users who want to run or test the Machine Learning function will need to prepare their own dataset using the same input format required by the system.

---

If real data is used during development, it should be stored locally and excluded from the repository using `.gitignore`.

Example `.gitignore` entries:

```text
real_dataset.csv
testing_dataset.csv
student_data.csv
*.xlsx
*.pkl
__pycache__/
.env
```

---

## Technologies Used

This project uses the following technologies:

* Python
* Flask
* HTML
* CSS
* Pandas
* NumPy
* Scikit-learn
* Machine Learning: Decision Tree Classifier

---

## How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ScholarMatch.git
```

Then go into the project folder:

```bash
cd ScholarMatch
```

---

### 2. Install Required Libraries

Install the required Python libraries:

```bash
pip install -r requirements.txt
```

If `requirements.txt` does not exist yet, create one and include:

```text
Flask
pandas
numpy
scikit-learn
```

---

### 3. Run the Flask Application

Run the project using:

```bash
python app.py
```

The system will usually run at:

```text
http://127.0.0.1:5000
```

Open the link in a web browser to use ScholarMatch.

---

## How the System Works

The system works through the following steps:

1. The user opens the ScholarMatch web application.
2. The user views scholarship information pages such as MARA, PTPTN, and JPA.
3. The user goes to the ScholarMatch Finder page.
4. The user enters details such as CGPA, family income, co-curricular score, programme, and year of study.
5. The input is submitted to the Flask backend.
6. The Machine Learning model processes the input.
7. The system predicts a suitable scholarship category.
8. The recommendation result is displayed to the user.

---

## Example User Input

Example input entered by the user:

```text
CGPA: 3.75
Family Income: RM1800
Co-curricular Score: 8
Programme: IT
Year of Study: 2
```

---

## Example Output

Example recommendation result:

```text
Recommended Scholarship: MARA
```

The output is displayed on the result page after the system processes the user input.

---

## Limitations

This project is developed for academic purposes and has several limitations:

* The recommendation accuracy depends on the size and quality of the dataset.
* The system currently focuses only on MARA, PTPTN, and JPA.
* The sample dataset is limited and used only for demonstration.
* The system does not guarantee actual scholarship approval.
* Scholarship requirements may change over time.
* The recommendation result should be used as guidance only.

---

## Future Improvements

Future improvements may include:

* Adding more scholarship providers.
* Increasing the dataset size.
* Improving the Machine Learning model accuracy.
* Adding user login and registration.
* Adding an admin panel to manage scholarship information.
* Adding a database to store scholarship records.
* Improving mobile responsiveness.
* Adding real-time scholarship application links.
* Adding model evaluation results to show prediction performance.

---

## Academic Purpose

This project is developed as a Final Year Project for academic purposes. It demonstrates how a Machine Learning model can be integrated into a Flask web application to provide scholarship recommendations based on student information.

ScholarMatch is intended as a prototype system and should be improved further before being used in a real scholarship application environment.

---

## Author

Developed by:

```text
Nurfatihah Hamzah
Final Year Project, Semester 2, 2025/2026
Supervised by Asst. Prof. Dr. Takumi Sase
Kulliyyah of Information and Communication Technology
International Islamic University Malaysia
```

---

## Disclaimer

ScholarMatch provides scholarship recommendations based on the available dataset and Machine Learning model. The recommendation does not guarantee scholarship approval.

Students should always refer to the official scholarship websites for the latest eligibility requirements, application procedures, deadlines, and terms and conditions.
