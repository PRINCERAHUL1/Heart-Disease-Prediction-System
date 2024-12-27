# 💚 Heart Disease Prediction System ❤️

## 📋Description
The **Heart Disease Prediction System** is a machine learning-based project designed to predict the likelihood of heart disease based on various health-related parameters. This system leverages predictive analytics to assist medical professionals and individuals in assessing potential heart-related risks, fostering timely intervention and diagnosis.

## 🚀Features
- 🧠 **Accurate Predictions**: Predicts the risk of heart disease based on input parameters with high precision.
- 🤖 **Machine Learning Model**: Implements a pre-trained machine learning model trained on healthcare data.
- 🌟 **Interactive User Interface**: Built with Streamlit for a clean and interactive UI.
- 📊 **User Data Input**: Supports multiple input methods including sliders, number inputs, and dropdowns for flexibility.
- 🔍 **Real-Time Prediction**: Instantly displays prediction results with visual cues (icons and colors).

## 💻Technologies Used

![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Model-brightgreen)

- **Programming Language:**
  - ![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
- **Libraries:** 
  - ![Pandas](https://img.shields.io/badge/Library-Pandas-green?logo=pandas&logoColor=white)
  - ![NumPy](https://img.shields.io/badge/Library-NumPy-orange?logo=numpy&logoColor=white)
  - ![Scikit-learn](https://img.shields.io/badge/Library-Scikit%20Learn-purple?logo=scikit-learn&logoColor=white)
  - ![Matplotlib](https://img.shields.io/badge/Library-Matplotlib-yellow?logo=matplotlib&logoColor=white)
  - ![Seaborn](https://img.shields.io/badge/Library-Seaborn-pink?logo=seaborn&logoColor=white)
- **Tools**:
  - ![Google Colab](https://img.shields.io/badge/IDE-Google%20Colab-cyan?logo=googlecolab&logoColor=white)
  - ![Jupyter Notebook](https://img.shields.io/badge/Jupyter-Notebook-black?logo=jupyter&logoColor=white)
  - ![VS Code](https://img.shields.io/badge/IDE-VS%20Code-navy?logo=visual-studio-code&logoColor=white)
- **Deployment**:
   - ![Streamlit](https://img.shields.io/badge/Deployment-Streamlit-red?logo=streamlit)


## 🎯Dataset
The dataset used for this project contains health-related parameters like:
- Age: Age of the patient in years.
- Sex: Gender of the patient.
- Chest Pain Type: Type of chest pain experienced (0-3).
- Resting Blood Pressure: Resting blood pressure in mm Hg.
- Serum Cholesterol: Serum cholesterol in mg/dl.
- Fasting Blood Sugar: Fasting blood sugar > 120 mg/dl (1 = true; 0 = false).
- Resting ECG Results: Resting electrocardiographic results (0-2).
- Max Heart Rate Achieved: Maximum heart rate achieved.
- Exercise Induced Angina: Presence of exercise-induced angina (1 = yes; 0 = no).
- ST Depression: Value of ST depression induced by exercise relative to rest.
- Slope of the Peak Exercise ST Segment: Slope of the peak exercise ST segment (0-2).
- Number of Major Vessels Colored by Flourosopy: Number of major vessels (0-4).
- Thalassemia: A blood disorder (0-3).


## 🛠️Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/PRINCERAHUL1/Heart-Disease-Prediction-System.git
   cd Heart-Disease-Prediction-System
   ```

2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit Application:
   ```bash
   streamlit run main.py
   ```

## 📥Usage
1. Input health-related parameters through the system's interface.
2. The model processes the input data and provides a prediction on the likelihood of heart disease.

## 🧪Model Training
- The machine learning model was trained using the **Scikit-learn** library.
- Algorithms tested include **Logistic Regression**, **Decision Trees**, **Random Forest**, and **Support Vector Machines (SVM)**.
- The model with the best performance (highest accuracy and precision) was selected for the final implementation which was **Random Forest**.

## 📊Results
- Model Accuracy: **97%**
- Confusion Matrix, Precision, Recall, and F1 Score were used to evaluate the model.

## 🤝Contributing
Contributions are welcome! Feel free to fork this repository and submit a pull request.
1) Fork the Repository
2) Create your Feature Branch
3) Commit your Changes
4) Push to the Branch
5) Open a Pull Request

## 🙏Acknowledgements
- Dataset sourced from `UCI Machine Learning Repository`.
- Inspiration and guidance from open-source communities.

## License
This project is licensed under the [MIT License](LICENSE).

## 📧 Contact
Rahul Mandal - rmrahul258@gmail.com
