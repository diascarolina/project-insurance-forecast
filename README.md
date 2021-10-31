# Health Insurance Price Forecast

[<img src="https://img.shields.io/badge/author-Carolina%20Dias-FB3799?style=flat-square"/>](https://github.com/diascarolina) [<img src="https://img.shields.io/badge/carodias-0A66C2?style=flat-square&logo=linkedin&logoColor=white" />](https://www.linkedin.com/in/carodias/) [![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=flat-square&logo=Jupyter)](https://jupyter.org/try) [![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg?style=flat-square)](https://github.com/diascarolina/project-insurance-forecast/blob/main/LICENSE)

![](img/poster.jpg)

# Table of Contents

1. [Problem Context](problem-context)
2. [Project Organization](project-organization)
3. [How to Run it Locally](how-to-run-it-locally)
4. [Deployment with Heroku](deployment-with-heroku)
5. [To Do](to-do)
6. [References](references)
7. [Contacts](contacts)

# 1 Problem Context

Today, as prices rise for basic necessities, we need to have a way to check beforehand what we will spend our money on. For medical insurance we can take a look at various features to arrive at a price for customers. This is what we'll do in this project, from prediction to deployment.

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


The variable we want to predict is from the column **charges**.

This type of price prediction is very useful both for the company that sells insurance and for the person buying the insurance, so every part involved in the process can have a baseline for how much they would pay or receive for the transaction. This is where data science shines, in solving different bussiness problems.

# 2 Project Organization

### 🟢 [Main **notebook** containing the **EDA** and the training and tuning of the Machine Learning **models**](https://github.com/diascarolina/project-insurance-forecast/blob/main/notebook.ipynb)

### 🟢 [The script to **train** and **save** the chosen model](https://github.com/diascarolina/project-insurance-forecast/blob/main/train.py)

### 🟢 [The code for the **Flask** app capable of making **predictions**](https://github.com/diascarolina/project-insurance-forecast/blob/main/predict.py)

### 🟢 [You can use this script to test the **requests** for the **predictions**](https://github.com/diascarolina/project-insurance-forecast/blob/main/make_requests.py)

### 🟢 [Our final **Dockerfile**](https://github.com/diascarolina/project-insurance-forecast/blob/main/Dockerfile)

### 🟢 [The code for the **Streamlit** application](https://github.com/diascarolina/project-insurance-forecast/blob/main/streamlit_app.py)

# 3 How to Run it Locally

Generally, the commands here should be run within a terminal. To begin you need to **clone this repo in your local computer and go into the project-insurance-forecast directory**.

To clone this repository:
```bash
git clone https://github.com/diascarolina/project-insurance-forecast.git
```

or for cloning via SSH use:
```bash
git clone git@github.com:diascarolina/project-insurance-forecast.git
```

If you are unsure which method to use for cloning, the first one is enough.

If you are at the directory where you issued the cloning command, type the following on your terminal:

```bash
cd project-insurance-forecast
```

This will bring you into our `project-insurance-forecast` directory.

The environment and dependency manager used in this project is `Pipenv`. If you don't have it already installed, you can do it using (assuming Python is already installed in the system)

```bash
pip3 install pipenv
```

If it doens't work, you can try

```bash
pip install pipenv
```

Now, at the project directory, we can install the necessary libraries and dependencies from the **Pipfile** using:

```bash
pipenv install
```

If you want to run the notebook, use the following command to install the extra dependencies:

```bash
pipenv install --dev
```

Now activate the environment:

```bash
pipenv shell
```

Our project already has the `.bin` file for the model, but if you want to retrain the model and resave the model you can do it by running

```bash
python train.py
```

To deploy the Flask app locally we can do it directly or we can do it using `gunicorn`. To run it directly

```bash
python predict.py
```

or using `gunicorn` (recommended)

```bash
gunicorn --bind 0.0.0.0:9696 predict:app
```

So, the project should then be running locally at http://localhost:9696.

To test the app using a POST request we have many options: run the `make_requests.py` script, use `curl` or we can use Postman. Let's see the first two.

To run the script to make the request:

```bash
python make_request.py
```

Using `curl` (you can change the values of the parameters):

```bash
curl -X POST http://localhost:9696/predict \
-H 'Content-Type: application/json' \
-d '{"age": 19, "sex": "female", "bmi": 25, "children": 1, "smoker": "no", "region": "northwest"}'
```

That's it! If you want, you can explore it more and deploy the Streamlit app locally using

```bash
streamlit run streamlit_app.py
```

Finally, we can build and run the Docker image locally with the Dockerfile provided (next we'll do it with Docker Hub).

To build a Docker image called "insurance-forecast":

```bash
docker build -t insurance-forecast .
```

To run it:

```bash
docker run -it --rm -p 9696:9696 insurance-forecast
```

Or you can pull the image directly from [Docker Hub](https://hub.docker.com/repository/docker/diascaro/insurance-forecast) (without having to build it first):

```bash
docker run -it --rm -p 9696:9696 diascaro/insurance-forecast
```

You can test it as the above with the `make_requests.py` script and choosing the first option to test it locally.

# 4 Deployment with Heroku

The API was deployed to the cloud using Heroku. The reason for chosing Heroku is because it is free.

🟢 [Click here to access the main page of the app](https://insurance-forecast.herokuapp.com/)

To make a POST request to the URL `https://insurance-forecast.herokuapp.com/predict` we can also use our `make_requests.py` script, or `curl` or use Postman. Again, let's see the first two methods.

Run the following script and choose the second option (2):

```bash
python make_request.py
```
Or using `curl` (you can change the values of the parameters):

```bash
curl -X POST https://insurance-forecast.herokuapp.com/predict \
-H 'Content-Type: application/json' \
-d '{"age": 19, "sex": "female", "bmi": 25, "children": 1, "smoker": "no", "region": "northwest"}'
```


## Bonus: Streamlit App

We also have an app using Streamlit, an open-source Python library used to facilitate the deployment of apps.

🟢 [Click here to access the Streamlit app](https://share.streamlit.io/diascarolina/project-insurance-forecast/main)

You don't need to make a request, you can fill the details directly on the app :D

# 5 To Do

- [ ] Separate the files into folders for better organization

- [ ] Try to deploy the Flask app and the Streamlit app into the same URL

# 6 References

- [Image by Olya Kobruseva on Pexels](https://www.pexels.com/pt-br/foto/calendario-flatlay-tendencia-flat-lay-dentro-de-casa-7163953/)
- [Machine Learning Zoomcamp](https://datatalks.club/courses/2021-winter-ml-zoomcamp.html)
- [ML Zoomcamp: Midterm Project info](https://github.com/alexeygrigorev/mlbookcamp-code/tree/master/course-zoomcamp/07-midterm-project)
- [Kaggle Original Problem](https://www.kaggle.com/mirichoi0218/insurance)
- [Deploy Churn Service on Heroku](https://github.com/razekmaiden/churn_service_heroku)
- [Markdown to HTML](https://markdowntohtml.com/)
- [Markdown CSS](https://markdowncss.github.io/)

# 7 Contacts

Any tips or suggestions? Feel free to contact me!

[<img src="https://img.shields.io/badge/diascarolina-000000?style=flat-square&logo=github&logoColor=white" />](https://github.com/diascarolina) [<img src="https://img.shields.io/badge/carodias-0A66C2?style=flat-square&logo=linkedin&logoColor=white" />](https://www.linkedin.com/in/carodias/) [<img src="https://img.shields.io/badge/Gmail-EA4335?style=flat-square&logo=Gmail&logoColor=white" />](mailto:carolinadiasw@gmail.com)
