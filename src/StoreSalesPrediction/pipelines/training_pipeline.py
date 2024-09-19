from src.StoreSalesPrediction.components.data_ingestion import DataIngestion
from src.StoreSalesPrediction.components.data_transformation import DataTransformation
from src.StoreSalesPrediction.components.model_trainer import ModelTrainer
from src.StoreSalesPrediction.components.data_preprocessing import DataCleaning  # Add import for DataCleaning

import os
import sys
from src.StoreSalesPrediction.logger import logging
from src.StoreSalesPrediction.exception import customexception

if __name__ == "__main__":
    try:
        # Data Cleaning
        data_cleaning = DataCleaning()
        train_df, test_df = data_cleaning.initiate_data_cleaning()
        logging.info(f"Data Cleaning completed. Cleaned Train Data: {data_cleaning.cleaning_config.train_data_path_cleaned}, Cleaned Test Data: {data_cleaning.cleaning_config.test_data_path_cleaned}")

        # Data Ingestion
        obj = DataIngestion()
        raw_data_path, train_data_path, test_data_path = obj.initiate_data_ingestion()
        logging.info(f"Data Ingestion completed. Raw Data: {raw_data_path}, Train Data: {train_data_path}, Test Data: {test_data_path}")

        # Data Transformation
        data_transformation = DataTransformation()
        train_arr, test_arr, preprocessor_file = data_transformation.initiate_data_transformation()
        logging.info("Data Transformation completed.")

        # Model Training
        model_trainer_obj = ModelTrainer()
        model_trainer_obj.initiate_model_trainer(train_arr, test_arr)
        logging.info("Model Training completed.")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        print(f"An error occurred: {e}")
