from flask import Flask
from flask import request
from flask import jsonify
import pandas as pd
import pickle


model_file = 'model_randomforestregressor.bin'

with open(model_file, 'rb') as f_in:
    model = pickle.load(f_in)


app = Flask('forecast')

@app.route('/predict', methods = ['POST'])
def predict():
    data = request.get_json()

    df = pd.DataFrame(data.items()).T
    df.columns = df.iloc[0]
    df = df.drop(df.index[0])
    df.reset_index(drop = True)

    df.sex = df.sex.map({"female": 1, "male": 0})
    df.region = df.region.map({'southwest': 0, 'southeast': 1, 'northwest': 2, 'northeast': 3})
    df.smoker = df.smoker.map({"yes": 1, "no": 0})

    prediction = model.predict(df)
    
    result = {
        "charges": prediction.tolist()[0]
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug = True, host = '0.0.0.0', port = 9696)