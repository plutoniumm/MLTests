# penicillin-prediction
Test repository for exploring Penicillin production prediction

# Ref Paper
https://www.sciencedirect.com/science/article/pii/S0098135418305106#tbl0001


## Todos
- Send Dataset/Inputs+Outputs & Expected Results
- DNN -> 1v-Regr (explore+ more)

## Regression
- Descaling data reduces accuracy from 6% to 0.

Accuracies
| |   R2             | MAE | MSE |
|--|----------------|---------|------------|
|SGD Regression | 0.9700 |  0.0345     |     0.0472 |
|Linear Regrn | 0.9726 |  0.0326     |     0.0451       |
|Decision Tree | 0.9937 |  0.0079     |     0.0216       |

## Tuning
**XGBoost:**
```python
# Tuning
param_grid = {'n_estimators': list(range(40,100,5)),
              'max_depth': list(range(4,10,1)),
              'reg_lambda' : [x / 100 for x in range(18,30,2)]
             }

grid = GridSearchCV(xg.XGBRFRegressor(), param_grid, refit = True, verbose = 3, n_jobs=-1) #
regr_trans = TransformedTargetRegressor(regressor=grid, transformer=QuantileTransformer(output_distribution='normal'))

# fitting the model for grid search
grid_result=regr_trans.fit(xtrain, ytrain)
best_params=grid_result.regressor_.best_params_
print(best_params) # RESULT: {'max_depth': 4, 'n_estimators': 85, 'reg_lambda': 0.18} # 75min
best = {'max_depth': 4, 'n_estimators': 85, 'reg_lambda': 0.18};
```
**GradientBoostingRegr:**
```py
param_grid = {'n_estimators': list(range(60,90,5)),
              'learning_rate' : [x / 100 for x in range(5,30,5)],
              'max_depth': list(range(4,10,1))
             }

grid = GridSearchCV(GradientBoostingRegressor(), param_grid, refit = True, verbose = 0, n_jobs=-1) #
regr_trans = TransformedTargetRegressor(regressor=grid, transformer=QuantileTransformer(output_distribution='normal'))

# fitting the model for grid search
grid_result=regr_trans.fit(xtrain, ytrain)
best_params=grid_result.regressor_.best_params_
print(best_params) # {'learning_rate': 0.25, 'max_depth': 7, 'n_estimators': 80}; 64min
best = {'learning_rate': 0.25, 'max_depth': 7, 'n_estimators': 80}
```
**RandomForest:**
```py
param_grid = {'n_estimators': list(range(40,120,5)),
              'max_depth': list(range(2,8,1))
             }

grid = GridSearchCV(RandomForestRegressor(), param_grid, refit = True, verbose = 3, n_jobs=-1) #
regr_trans = TransformedTargetRegressor(regressor=grid, transformer=QuantileTransformer(output_distribution='normal'))

# fitting the model for grid search
grid_result=regr_trans.fit(xtrain, ytrain)
best_params=grid_result.regressor_.best_params_
print(best_params) # {'max_depth': 7, 'n_estimators': 65} # 25 min
best = {'max_depth': 7, 'n_estimators': 65}
```


Accuracy
|                | Deep NN | Regression |
|----------------|---------|------------|
| **Tollerance** |         |            |
| 10%            | 63%     | 92%         |
| 1%             | 7%      | 70%        |
| *0.1%          | 0.7%    | 18%        |
\*: Target

<style>
    tr:nth-child(2) td:nth-child(2){
        background: #2f2;
        color: #fff;
    }
    tr:nth-child(3) td:nth-child(2){
        background: #ff4;
        color: #000;
    }
    tr:nth-child(4) td:nth-child(2){
        background: #f44;
        color: #fff;
    }
</style>