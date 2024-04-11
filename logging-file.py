import  logging

logging.basicConfig(level=logging.DEBUG,
                    filename="app.log",
                    filemode="a",
                    format='%(asctime)s-%(levelname)s-%(message)s')


logging.debug("the function has been well executed")
logging.info("Message for general information")
logging.warning("Attention")
logging.error("An error occurred")
logging.critical("Critical error")
