# Diabetes Prediction Project

This repository contains a diabetes prediction application built using machine learning and deployed via **Streamlit**. The project aims to predict the likelihood of diabetes based on input features, such as pregnancies, glucose level, blood pressure, and more.

## Features

- **Data Processing**: Handles and preprocesses the diabetes dataset (`diabetes.csv`).
- **Machine Learning Model**: A predictive model trained using scikit-learn to classify diabetes likelihood.
- **Interactive Web Application**: User-friendly Streamlit app for input and prediction.

## Try the App

You can try the live version of this app here: [Diabetes Prediction App](https://diabetes-predictor-h.streamlit.app/)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/hamdii10/diabetes-predictor.git
   cd diabetes-predictor
   ```

2. **Set up a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/macOS
   venv\Scripts\activate     # For Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
## Project Structure

```
diabetes-predictor/
├── app/                      # Application scripts
│   └── app.py                # Streamlit application script
├── data/                     # Dataset and related files
│   └── diabetes.csv          # Dataset used for training the model
├── models/                   # Machine learning models
│   └── model.pkl             # Saved machine learning model
├── notebooks/                # Jupyter notebooks for analysis and training
│   └── Diabetes.ipynb        # Notebook for data processing and model training
├── README.md                 # Project overview and instructions
├── LICENSE                   # License file
└── requirements.txt          # Python dependencies for the project
```

## How to Run

1. **Start the Streamlit app**:
   ```bash
   streamlit run app/app.py
   ```

2. **Enter input values**:
   - Number of times pregnant
   - Plasma glucose concentration
   - Diastolic blood pressure (mm Hg)
   - Triceps skin fold thickness (mm)
   - 2-Hour serum insulin (mu U/ml)
   - Body mass index (BMI)
   - Diabetes pedigree function
   - Age

3. **Predict**:
   - Click the "Predict" button to view the results.

## Dataset

The project uses the **Pima Indians Diabetes Dataset**, which is publicly available on Kaggle. It contains several medical predictor variables and one target variable that indicates the presence of diabetes.

**Dataset Link**: [Pima Indians Diabetes Dataset on Kaggle](https://www.kaggle.com/datasets/mathchi/diabetes-data-set/data)

## Model Details

The machine learning model was trained on the Pima Indians Diabetes dataset (`data/diabetes.csv`) and includes the following steps:
- Data preprocessing
- Feature engineering
- Training using a classification algorithm
- Saving the model (`models/model.pkl`) for deployment

## Deployment

The application is deployed locally using **Streamlit**. 

## Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests with improvements.

## License

This project is licensed under the MIT License. See `LICENSE` for more details.

## Contact

For questions or suggestions, reach out to:
- **Email**: ahmed.hamdii.kamal@gmail.com
