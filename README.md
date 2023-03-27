# SportsPlayerPredictionAnalysis

The repository contains an implementation of a soccer player prediction model that utilizes xgboost regressor algorithm to predict the overall rating of a football player.<br />
The algorithm uses features such as  potential, passing, dribbling and attacking scores to predict the overall rating. 

# Instructions
To use the model in your application, fork the repository and use the file ***fifamodeltrained.pkl***. It is contained in the streamapplication directory.<br />
If you want to test the application, fork/download the repository, and cd into streamapplication directory. <br />
Run ***streamlit run streamApp.py*** on the Vscode Terminal <br />
The implementation codes are contained in the ***player_prediction.ipynb***

# Model Performance Metrics <br />
  {'learning_rate': 0.15, 'max_depth': 5, 'n_estimators': 150, 'reg_alpha': 1, 'reg_lambda': 0} <br />
  Root Mean Square Error: 1.2100500363924542 <br />
  Meam Absolute Error: 0.8290837172906761 <br />
  Mean Square Error: 1.46422109057338  <br />
