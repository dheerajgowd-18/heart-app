🫀 Heart Disease Prediction App

A machine learning-powered Streamlit web application that predicts the likelihood of heart disease based on medical attributes such as age, cholesterol levels, blood pressure, and more.
The app is user-friendly, explains each medical term, and displays prediction results along with model accuracy.

🚀 Features

📊 Interactive Input Form – Enter patient details in a clean, guided interface.

📖 Medical Term Glossary – Understand terms like cp (Chest Pain Type), trtbps (Resting Blood Pressure), etc.

🔍 ML Prediction – Uses an XGBoost model trained on a heart disease dataset.

📈 Accuracy Display – Shows the trained model’s accuracy score.

☁️ Deployed on Streamlit Cloud – Accessible from any device.

📂 Project Structure
heart_app/
│── app.py                     # Streamlit frontend
│── heart_disease_model.pkl    # Trained ML model
│── requirements.txt           # Dependencies
│── README.md                  # Project documentation
└── .streamlit/config.toml     # (Optional) Custom theme

⚙️ Installation & Running Locally
1️⃣ Clone the repository
git clone https://github.com/<your-username>/heart-app.git
cd heart-app

2️⃣ Create and activate a virtual environment
python -m venv venv
# Activate (Windows)
venv\Scripts\activate
# Activate (Mac/Linux)
source venv/bin/activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run the Streamlit app
streamlit run app.py

🌐 Deployment

This project is deployed on Streamlit Cloud.
To deploy your own version:

Push this project to a GitHub repository.

Go to Streamlit Cloud, log in, and click "New App".

Select your repo, branch, and app.py as the entry point.

Deploy 🚀.

📊 Model Details

Algorithm: XGBoost Classifier

Training Data: Heart disease dataset (UCI Machine Learning Repository)

Metrics: Accuracy ~ XX% (replace with your actual score)

🧾 Glossary of Terms
Abbreviation	Meaning
age	Age of the patient
sex	Gender (1 = male, 0 = female)
cp	Chest Pain type
trtbps	Resting Blood Pressure (mm Hg)
chol	Serum Cholesterol (mg/dl)
fbs	Fasting Blood Sugar (>120 mg/dl, 1 = true, 0 = false)
restecg	Resting ECG results
thalachh	Maximum Heart Rate achieved
exng	Exercise induced angina (1 = yes, 0 = no)
oldpeak	ST depression induced by exercise
slp	Slope of the peak exercise ST segment
caa	Number of major vessels colored by fluoroscopy
thall	Thalassemia type
🛠️ Technologies Used

Python 3.10+

Streamlit

Pandas / NumPy

Scikit-learn

XGBoost

Joblib (model loading)

📜 License

This project is licensed under the MIT License – see the LICENSE file for details.

✨ Author

Your Name – Machine Learning Enthusiast
📧 Contact: dheerajgowd777@gmail.com
🔗 GitHub: @dheerajgowd-18
