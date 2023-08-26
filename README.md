# DiabeticPrediction
## Early Diabetic Prediction Based on Syntomps

This project is carried out with the process:
1. Data Loading
2. Exploratory Data Analysis (EDA)
3. Data Preparation (including *Encoding*, *Split*, and *Standardization*)
4. Model Development
   * Variations of algorithms are used to compare the performance between them, such as:
     * K-Nearest Neighbor (KNN)
     * Support Vector Machine (SVM)
     * Decision Tree
     * Random Forest (used in deployment)
     * AdaBoost
     * Neural Network
5. Model Evaluation (using *Accuracy*, *F1 Score*, *Recall* and *Precision*)
6. Deployment (using Flask and simple html website)

#### This project is built with:
1. Python
2. HTML & CSS
3. Scikit-Learn
4. TensorFlow
5. Seaborn
6. Pandas
7. Matplotlib
8. Numpy
9. Flask


### How to use:
1. Install requirement above
2. run this in terminal (inside the folder)
   
   `set FLASK_APP=app.py`
   
   `flask run`
3. Enter every input value
4. click "submit"
#### Dataset Link: https://www.kaggle.com/datasets/andrewmvd/early-diabetes-classification
##### Note: some improvement might be useful, for example using hyperparameter tuning methods like *Grid Search* for more optimized results or using cross-validation methods like *K-Fold* for a more convincing result
