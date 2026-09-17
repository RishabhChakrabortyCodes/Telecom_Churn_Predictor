import pandas as pd
import kagglehub
from kagglehub import KaggleDatasetAdapter

class DataLoaderError(Exception):
    pass

class DatasetLoader:
    def load(self, file_path=""):
        try:
            df = kagglehub.load_dataset(
            KaggleDatasetAdapter.PANDAS,
            "blastchar/telco-customer-churn",
            file_path,
            )

            return df
        except Exception as e:
            raise DataLoaderError("Data could not be loaded. Either the Kaggle API is not working or the  file path is incorrect or both.") from e
    
class DatapointLoader:
    def load(json_obj):
        try:
            df = pd.DataFrame([json_obj])
            return df
        except Exception as e:
            raise DataLoaderError("Invalid JSON object") from e