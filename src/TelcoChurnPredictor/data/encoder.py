import pandas as pd

class InvalidInput(Exception):
    pass

class Encoder:
    def encode(df:pd.DataFrame):
        if df is None or not isinstance(df, pd.DataFrame):
            raise InvalidInput("Invalid DataFrame passed.")
        # Binary Encoding
        binary_columns = ['gender', 'Partner', 'Dependents', 'PhoneService', 'PaperlessBilling', 'Churn']
        df[binary_columns] = df[binary_columns].replace({'Male':1, 'Female':0, 'Yes':1, 'No':0})

        # One Hot Encoding
        multicat_columns = ['MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract', 'PaymentMethod']
        df = pd.get_dummies(df, columns=multicat_columns, drop_first=True)

        return df