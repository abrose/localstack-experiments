import json
import logging
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, context):
    try:
        logger.info(f"## ENVIRONMENT VARIABLES {os.environ}")
        logger.info(f"## EVENT {event}")
        logger.info(f"## CONTEXT {context}")
        if event and "Records" in event:
            for elt in event["Records"]:
                logger.info(elt["body"])
        return True
    except Exception as e:
        logger.error(e)
        raise e

