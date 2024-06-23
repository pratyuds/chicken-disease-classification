from src.ChickenDiseaseCNNClassifier.logging import logger
from src.ChickenDiseaseCNNClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.ChickenDiseaseCNNClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
        logger.info(f">>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<\n\nx======================x")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Prepare Base Model"

if __name__ == '__main__':
    try:
        logger.info(f">>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<\n\nx======================x")
    except Exception as e:
        logger.exception(e)
        raise e