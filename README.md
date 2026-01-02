# 🚀 End-to-End Machine Learning Web Application
### (Score_Prediction)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Framework](https://img.shields.io/badge/Framework-Flask-green)
![ML](https://img.shields.io/badge/Library-Scikit--Learn-orange)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

> **A complete Data Science lifecycle project: From Data Ingestion to Deployment.**

## 🔍 Project Overview
This project demonstrates a **real-world industry-level Machine Learning workflow**. It is a modular, scalable, and deployable web application that takes user input via a web interface and predicts **[Insert Prediction Target, e.g., Student Test Scores / House Prices]**.

The goal is to simulate a professional environment by moving beyond simple Jupyter notebooks and building a production-ready pipeline including data transformation, model training, logging, exception handling, and a Flask web interface.

---

## ✨ Key Features
* **Modular Architecture:** Code is organized into components (Ingestion, Transformation, Training) for maintainability.
* **Automated Pipeline:** Seamless flow from raw data to a trained model.
* **Robust Error Handling:** Custom `exception.py` script to track errors and line numbers efficiently.
* **Logging:** Centralized `logger.py` to monitor execution and debug issues.
* **Web Interface:** A user-friendly HTML/CSS frontend built with Flask.
* **CI/CD Ready:** Structured to be easily deployed to clouds like AWS, Azure, or Render.

---

## 🏗️ Project Architecture

```
Score_Prediction/
│
├── artifacts/             # Stores generated files (CSV data, .pkl models)
├── catboost_info/         # CatBoost training logs and metadata
├── notebook/              # Jupyter notebooks for EDA and experimentation
├── src/                   # Source code for the project
│   ├── components/        # Core ML components
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   ├── model_trainer.py
│   │
│   ├── pipeline/          # Execution pipelines
│   │   ├── train_pipeline.py
│   │   ├── predict_pipeline.py
│   │
│   ├── exception.py       # Custom exception handling
│   ├── logger.py          # Logging configuration
│   └── utils.py           # Helper functions (save/load objects)
│
├── templates/             # HTML Frontend
├── static/                # CSS/Images
├── application.py         # Flask App entry point
├── requirements.txt       # Project dependencies
├── setup.py               # Package setup
└── README.md              # Project documentation
```
⚙️ Technologies 
UsedCategory           Technologies
Language          __>> Python 3.x
Data Manipulation __>> Pandas, NumPy
Machine Learning  __>> Scikit-learn, CatBoost, XGBoostWeb 
Framework         __>> Flask
Frontend          __>> HTML, CSS
Utilities         __>> Pickle, OS, Sys, Logging


🔄 The Machine Learning Pipeline

1️⃣ Data Ingestion (data_ingestion.py)
Reads the raw dataset from the source.

Performs train-test split.

Saves the split data into the artifacts/ folder.

2️⃣ Data Transformation (data_transformation.py)
Handles missing values and outliers.

Performs One-Hot Encoding and Scaling.

Saves the preprocessor object (preprocessor.pkl) for future use.

3️⃣ Model Training (model_trainer.py)
Trains multiple models (Random Forest, Decision Tree, CatBoost, etc.).

Evaluates models using R2 Score / Accuracy.

Selects the best performing model and saves it as model.pkl.

4️⃣ Prediction (predict_pipeline.py)
Loads the saved preprocessor.pkl and model.pkl.

Accepts new user data from the web form.

Processes the input and returns the prediction.

📊 Model Performance
(Optional: Update this section with your actual results)

Best Model: Ridge	, Linear Regression	,CatBoosting, Regressor

Accuracy/R2 Score: 87.5%

📸 Screenshots
### Demo_1
![img_!](https://github.com/bhautik2005/ML_project2/blob/55bc24380d57bfea2f9fadb62bb5102ddfbbe4af/Screenshot%202025-12-16%20094118.png)

### Demo_2
![im2](https://github.com/bhautik2005/ML_project2/blob/55bc24380d57bfea2f9fadb62bb5102ddfbbe4af/Screenshot%202025-12-16%20094135.png)

 
🚀 How to Run the Project
Follow these steps to set up the project locally:

1. Clone the Repository
Bash

git clone [https://github.com/bhautik2005/ML_project2.git](https://github.com/bhautik2005/Score_Prediction.git)
cd ML_project2
2. Create a Virtual Environment
It is recommended to use a virtual environment to avoid dependency conflicts.

Windows:

Bash

python -m venv venv
venv\Scripts\activate
Linux / Mac:

Bash

python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
Bash

pip install -r requirements.txt
4. Run the Application
Bash

python application.py
5. Access the App
Open your browser and go to: http://127.0.0.1:5000

🤝 Author
Bhautik Gondaliya * GitHub: bhautik2005

Email: gondaliyabhautik419@gmail.com

📝 License
This project is licensed under the MIT License.
