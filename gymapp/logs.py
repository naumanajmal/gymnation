import logging

logger = logging.getLogger("audit")

def log_action(action: str, description: str):
    logger.info(f"ACTION: {action} | DESC: {description}")
