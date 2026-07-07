# Smart Lender - Loan Eligibility Prediction System Using Machine Learning

## 📌 Project Summary

Smart Lender is a Machine Learning-powered Loan Eligibility Prediction System developed to automate the preliminary loan screening process. Instead of manually reviewing every loan application, the system analyzes applicant information such as gender, marital status, education, employment status, applicant income, co-applicant income, loan amount, loan amount term, credit history, and property area to predict whether the applicant is eligible for a loan.

Rather than replacing loan officers, Smart Lender acts as an intelligent decision-support tool that enables faster, more consistent, and transparent lending decisions.

---

# ✨ Key Features

- Instant Loan Eligibility Prediction
- Machine Learning-based Decision Support
- User-Friendly Web Interface
- Data Preprocessing & Feature Engineering
- Multiple Machine Learning Algorithms Comparison
- High Accuracy using Random Forest Classifier
- Responsive HTML & CSS Interface
- Fast Prediction using Trained Model

---

# 🏗 Technical Architecture

The project follows a modular three-layer architecture.

## 1. Machine Learning Layer

Responsible for:

- Data Collection
- Data Cleaning
- Missing Value Handling
- Feature Encoding
- Feature Selection
- Model Training
- Model Evaluation
- Model Saving

### Algorithms Used

- Decision Tree Classifier
- Random Forest Classifier
- K-Nearest Neighbors (KNN)
- XGBoost Classifier

### Final Selected Model

**Random Forest Classifier**

---

## 2. Backend Layer

Implemented using **Flask**.

Responsibilities include:

- Handling HTTP Requests
- Receiving User Inputs
- Loading Trained Machine Learning Model
- Processing Prediction Requests
- Returning Loan Eligibility Results

---

## 3. Presentation Layer

Developed using:

- HTML5
- CSS3
- Jinja2 Templates

Provides a simple, clean, and responsive user interface for loan prediction.

---

# 👩‍💻 Project Submitted By

**Name:** Anusha Tippabathini

**Email:** josephanusha678@gmail.com

**Project Title:** Smart Lender - Loan Eligibility Prediction System Using Machine Learning

---

# 🚀 How to Run the Application

## Prerequisites

- Python 3.10 or above
- pip Package Manager
- Visual Studio Code (Recommended)

---

## Step 1: Navigate to the Project Folder

The complete source code is available inside the **SmartLender_Project_codes** folder.

```bash
cd SmartLender_Project_codes
```

---

## Step 2: Install Required Libraries

```bash
pip install -r requirements.txt
```

---

## Step 3: Train the Machine Learning Model

Run:

```bash
python model.py
```

This process will:

- Load the dataset
- Handle missing values
- Encode categorical data
- Train multiple Machine Learning models
- Compare model accuracy
- Save the best model as **loan_model.pkl**

---

## Step 4: Launch the Flask Application

```bash
python app.py
```

---

## Step 5: Open the Application

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

# 🧪 Testing

The application was tested using multiple loan applicant records.

Testing includes:

- Functional Testing
- Input Validation
- User Interface Testing
- Model Prediction Testing

All major functionalities passed successfully.

---

# 📊 Machine Learning Performance

| Algorithm | Accuracy |
|------------|----------|
| Decision Tree | 70.73% |
| Random Forest | 76.42% |
| K-Nearest Neighbors | 57.72% |
| XGBoost | 76.42% |

### Final Model

✅ Random Forest Classifier

---

# 📂 Project Structure

```
SmartLender
│
├── 1.Brainstorming and Ideation
├── 2.Requirement Analysis
├── 3.Project Design Phase
├── 4.Project Planning Phase
├── 5.Project Development Phase
├── 6.Project Testing
├── 7.Project Documentation
├── 8.Project Demonstration
│
├── SmartLender_Project_codes
│   ├── app.py
│   ├── model.py
│   ├── train.py
│   ├── result.py
│   ├── loan.csv
│   ├── loan_model.pkl
│   ├── requirements.txt
│   ├── templates
│   │   ├── index.html
│   │   └── result.html
│   └── static
│       └── style.css
│
└── README.md
```

---

# 📸 Project Screenshots

- Home Page
- Loan Eligibility Form
- Loan Approved Result
- Loan Rejected Result
- VS Code Project Structure

---

# 🔮 Future Scope

The Smart Lender project can be enhanced in several ways:

- Improve prediction accuracy using Deep Learning algorithms.
- Deploy the application on cloud platforms such as Render or AWS.
- Add user authentication and login functionality.
- Develop Android and iOS mobile applications.
- Integrate with banking APIs.
- Implement Explainable AI (XAI) to display prediction reasons.
- Improve the user interface using Bootstrap or React.

---

# 📚 Conclusion

The Smart Lender Loan Eligibility Prediction System successfully predicts whether a loan applicant is eligible for loan approval using Machine Learning techniques. The project demonstrates the practical implementation of data preprocessing, feature engineering, model training, evaluation, and deployment using Flask. Among all evaluated algorithms, the Random Forest Classifier achieved the highest performance and was selected as the final prediction model.

---

# 📄 License

This project is developed for educational and academic purposes only.

---

# 🙏 Acknowledgement

This project was developed as part of a Machine Learning learning journey to understand real-world loan eligibility prediction using Python, Flask, and Scikit-learn. It demonstrates the practical implementation of Machine Learning concepts in building an intelligent web application.