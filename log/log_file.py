import logging

class Log():

    def __init__(self):

        logging.basicConfig(filename="../logf.txt",
                            filemode='a',
                            format='%(asctime)s - %(message)s',
                            level=logging.INFO)
        self.logging=logging


