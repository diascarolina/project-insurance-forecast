# libraries
import pandas as pd
import numpy as np
import pickle

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import GridSearchCV

# constants
rs = 42847

# functions
def run_model(model, print_values = 1, return_predictions = 0):
    """
    Function that receives a machine learning model
    and returns its metrics.
    
    print_values = 1: print the results of the calculated metrics
    return_predictions = 1: returns the y predictions together with the metrics
    """
    model.fit(X_train, y_train)
    y_predictions = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_predictions)
    mse = mean_squared_error(y_test, y_predictions)
    rmse = np.sqrt(mse)
    if print_values:
        print(f"\tModel Metrics:")
        print(f"\tMAE: {round(mae, 3)}")
        print(f"\tMSE: {round(mse, 3)}")
        print(f"\tRMSE: {round(rmse, 3)}")
    if return_predictions:
        return y_preds, mae, mse, rmse
    return mae, mse, rmse


# load data
data_url = 'https://raw.githubusercontent.com/diascarolina/data-science-bootcamp/main/data/insurance.csv'

print('Loading data...\n')
df = pd.read_csv(data_url)

# prepare data
print('Preparing data...\n')
df = pd.get_dummies(df, columns = ['sex', 'region', 'smoker'])

X = df.drop('charges', axis = 1)
y = df.charges

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = rs)

# fit and train the model
print('Fitting and training the RandomForestRegressor...')
randomreg = RandomForestRegressor(random_state = rs)

params = {
    'n_estimators': [10, 20, 30],
    'max_features': ['auto', 'sqrt', 'log2'],
    'min_samples_split': [2, 4, 8],
    'bootstrap': [True, False]
}

rfr_search = GridSearchCV(randomreg,
                          params, 
                          scoring = 'neg_root_mean_squared_error',
                          error_score = 'raise',
                          n_jobs = -1,
                          verbose = 0,
                          cv = 5)

rfr_search.fit(X_train, y_train)

rfr_model = rfr_search.best_estimator_
mae_rfr, mse_rfr, rmse_rfr = run_model(rfr_model)
print('Finished modelling :D\n')

# save the model
print('Saving the model...\n')
model = rfr_model
output_file = 'model_randomforestregressor.bin'

with open(output_file, 'wb') as f_out:
    pickle.dump(model, f_out)

print(f'The model was saved to "{output_file}"')