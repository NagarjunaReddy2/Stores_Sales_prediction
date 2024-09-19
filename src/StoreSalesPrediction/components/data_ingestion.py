import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.StoreSalesPrediction.exception import customexception
from src.StoreSalesPrediction.logger import logging

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', "train.csv")
    test_data_path: str = os.path.join('artifacts', "test.csv")
    raw_data_path: str = os.path.join('artifacts', "data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            # Read the dataset
            df = pd.read_csv("notebooks/data/Train.csv")
            logging.info('Read the dataset as dataframe')

            # Create directories if they do not exist
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)

            # Save raw data
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            logging.info("Raw data saved")

            # Train-test split
            logging.info("Train-test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            # Save train and test data
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info("Train and test data saved")

            # Return paths
            return self.ingestion_config.raw_data_path, self.ingestion_config.train_data_path, self.ingestion_config.test_data_path
        
        except Exception as e:
            raise customexception(e, sys)

if __name__ == "__main__":
    obj = DataIngestion()
    try:
        raw_data_path, train_data_path, test_data_path = obj.initiate_data_ingestion()
        print(f"Raw Data Path: {raw_data_path}")
        print(f"Train Data Path: {train_data_path}")
        print(f"Test Data Path: {test_data_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
