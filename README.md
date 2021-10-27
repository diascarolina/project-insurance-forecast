# Medical Insurance Price Forecast

[<img src="https://img.shields.io/badge/author-Carolina%20Dias-FB3799?style=flat-square"/>](https://github.com/diascarolina) [<img src="https://img.shields.io/badge/carodias-0A66C2?style=flat-square&logo=linkedin&logoColor=white" />](https://www.linkedin.com/in/carodias/) [![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=flat-square&logo=Jupyter)](https://jupyter.org/try) [![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg?style=flat-square)](https://github.com/diascarolina/project-insurance-forecast/blob/main/LICENSE)

# Table of Contents

1. [Problem Context](#problem-context)
2. [Project Organization](#project-organization)
3. [How to Run it Locally](how-to-run-it-locally)
4. [Deployment with Docker and Heroku](deployment-with-docker-and-heroku)
5. 


# 1 Problem Context

Today, as prices rise and rise for basic necessities, we need to have a way to check beforehand what we will spend our money on. For medical insurance we can take a look at various features to arrive at a price for customers. This is what we'll do in this project, from prediction to deployment.

Our data was obtained from this [Kaggle problem on Medical Cost - Insurance Forecast](https://www.kaggle.com/mirichoi0218/insurance), in which we have the question of **"Can you accurately predict insurance costs?"**

> For ease of access, the data was upload to GitHub [here](https://github.com/diascarolina/project-insurance-forecast/blob/main/insurance.csv).

From this we see that we have the following information (adapted from the Kaggle problem description):

|  Column  |             Description             |
|:--------:|:-----------------------------------:|
|    **age**   |  Age of primary beneficiary  |
|    **sex**   |  Insurance contractor gender: female, male |
|    **bmi**   |  Body mass index, providing an understanding of body, weights that are relatively high or low relative to height, objective index of body weight $(kg/m^2)$ using the ratio of height to weight, ideally 18.5 to 24.9 |
|   **children**   | Number of children covered by health insurance / Number of dependents |
| **smoker** |    If that person smokes or not    |
| **region** |  The beneficiary's residential area in the US, northeast, southeast, southwest, northwest  |
|  **charges**  |  Individual medical costs billed by health insurance  |


The variable we want to predict is from the column **charges**

# 2 Project Organization

### 🟢 [Main **notebook** containing the **EDA** and the training and tuning of the Machine Learning **models**](https://github.com/diascarolina/project-insurance-forecast/blob/main/notebook.ipynb)

### 🟢 [The script to **train** and **save** the chosen model](https://github.com/diascarolina/project-insurance-forecast/blob/main/train.py)

### 🟢 [The code for the **Flask** app capable of making **predictions**](https://github.com/diascarolina/project-insurance-forecast/blob/main/predict.py)

### 🟢 [You can use this script to test the **requests** for **predictions**](https://github.com/diascarolina/project-insurance-forecast/blob/main/make_requests.py)

### 🟢 [Our final **Dockerfile**](https://github.com/diascarolina/project-insurance-forecast/blob/main/Dockerfile)

### 🟢 [The code for the **Streamlit** application](https://github.com/diascarolina/project-insurance-forecast/blob/main/streamlit_app.py)

# 3 How to Run it Locally



# 4 Deployment with Docker and Heroku

## Docker

- `docker build -t insurance-forecast -t`
- `docker run -it --rm -p 9696:9696 diascaro/insurance-forecast`


## POST Request

- You can also use Postman

# To Do

[] Separate the files into folders for better organization
[] Try to deploy the Flask app and the Streamlit app into the same URL

# References

- https://markdowntohtml.com/
- https://markdowncss.github.io/