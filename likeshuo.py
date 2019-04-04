import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

fileHandler = logging.FileHandler("./log.log")
fileHandler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)-12s - %(levelname)-8s - %(message)s")
fileHandler.setFormatter(formatter)
logger.addHandler(fileHandler)

streamHandler = logging.StreamHandler()
streamHandler.setFormatter(formatter)
streamHandler.setLevel(logging.CRITICAL)
logger.addHandler(streamHandler)
