## Telco Churn Predictor
#### Dataset: https://www.kaggle.com/datasets/blastchar/telco-customer-churn

In this project, we have tried to implement a churn predictor algorithm for the telecommunications industry. We have used the IBM Telco Churn Predictor dataset. 
Our approach has been pretty simple so far. We have first loaded the data, encoded the data using both Binary Encoding (for binary features) and One Hot Encoding (for multi-class features). 
Then we cleaned the Data. The main data cleaning activities were making sure all the data types were consistent, dropping unneeded features and  collapsing redundant columns into one column.
Then we analyzed the dataset by looking into the correlation analysis. We decided not to look into the multicolinearity since we will use tree based algorithms. 
Then we started with Model Development. Now, I decided that I will approach this project without using SMOTE. So, I used thresholding instead. We looked into Random Forest, LightGBM and XGBoost. For the most of the project we looked into maximizing the recall. However, because we lost a lot of the precision, right now we are trying to maximize ROC-AUC.
Right now our achieved metrics are well below the SOTA. We are taking inspiration right now from the paper: Machine Learning–Based Customer Churn Prediction in Telecommunication Industry by Mettle, Henry et. al.

## Reference Papers

**Mettle et al. (2026), "Machine Learning–Based Customer Churn Prediction in Telecommunication Industry"** — Compares Decision Tree, Random Forest, XGBoost, and Logistic Regression on the IBM Telco dataset, tuned via grid search + 5-fold CV, no resampling (relies on class weighting). Best model: Random Forest at 84.73% accuracy, 84.62% F1, 93.86% ROC-AUC. Note: some figures/tables in the paper appear inconsistent (dataset totals don't match across sections, and a few confusion matrices are mislabeled with breast-cancer class names), so treat their numbers as a rough benchmark rather than an exact target.

**Omar, Ogada & Tole (2026), "A Hybrid Feature Selection Framework for Dimensionality-Optimized Customer Churn Prediction"** — Focuses on cutting feature dimensionality rather than chasing top accuracy. Uses a 4-stage hybrid feature selection pipeline (Mutual Information → Recursive Feature Elimination → Boruta → Simulated Annealing) inside a nested 5×3 stratified cross-validation, with SMOTE applied only within outer training folds to avoid leakage. Tested on IBM Telco (28 features, an augmented variant with location data) and Cell2Cell (58 features). Best model (XGBoost): 81.60% accuracy / 0.818 F1 / 0.906 AUC-ROC on IBM Telco, while cutting features from 28 to 16; 77.52% accuracy / 0.752 F1 / 0.854 AUC-ROC on Cell2Cell, cutting features from 57 to 25.

