import os
import sys


try:
     from catboost import CatBoostRegressor
     _has_catboost = True
except ImportError:
     _has_catboost = False

from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor
)
from dataclasses import dataclass
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score
try:
     from xgboost import XGBRegressor
     _has_xgboost = True
except ImportError:
     _has_xgboost = False

from src.exception import CustomException
from src.logger import logging
from src.utils import evaluate_model, save_object

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifacts", "model.pkl")


class ModelTrainer:
     def __init__(self):
         self.model_trainer_config = ModelTrainerConfig()

     def initiate_model_trainer(self, train_array, test_array):
          try:
               logging.info("Split training and test input data")

               X_train,y_train,X_test,y_test =(
                     train_array[:,:-1],
                     train_array[:,-1],
                    test_array[:,:-1],
                    test_array[:,-1]
                             )
               models={
                    "Random Forest":RandomForestRegressor(),
                      "Decision Tree":DecisionTreeRegressor(),
                      "Gradient Boosting":GradientBoostingRegressor(),
                      "K-Neighbors Regressor":KNeighborsRegressor(),
                      "Linear Regression":LinearRegression(),
                      "AdaBoost Regressor":AdaBoostRegressor()
                }
               if _has_xgboost:
                      models["XGB Regressor"] = XGBRegressor()
               if _has_catboost:
                      models["CatBoost Regressor"] = CatBoostRegressor(verbose=False)
               
               model_report:dict= evaluate_model(X_train=X_train,y_train=y_train,X_test=X_test,y_test=y_test,models=models)

               best_model_score = max(sorted(model_report.values()))

               best_model_name = list(model_report.keys())[
                    list(model_report.values()).index(best_model_score)
                ]
               
               if best_model_score < 0.6:
                    raise CustomException("No best model found")
               logging.info("Best model found on both training and testing dataset")
               

               save_object (
                        file_path =  self.model_trainer_config.trained_model_file_path,
                        obj=models[best_model_name]
                        )
                     
               predictions = models[best_model_name].predict(X_test)

               r2_square = r2_score(y_test, predictions)
               return r2_square

          except Exception as e:
                raise CustomException(e, sys)
          
         
           