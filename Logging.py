"""
LOGGING: logging is a means of tracking events thta happen when some software runs.
logging is important for software developing, debugging and running. if we don't have
any logging record and your program crashes, there are less chance that we can detect
the cause of the problem.

why printing is not good option?
some developers use the concept of printing the statements to validate if the statement
are executed correctly or some error ha occurred. but printing is not a good idea as solve issue for
simple scripts but for complex scripts, the printing approach fails

python has built-in module logging which allows writing status message to a file or any other output strems.
the file contains the info on which part of the code is executed and what problems have been arisen

LEVELS OF LOG MESSAGE
there are five built-in levels of the log message
->debug: these are used to give detailed information, typically of interest only when diagonosing problems.
->Info: these are used to confirm that things are working as expected.
->Warning: these are used an indication that something unexpected happened, or is
indicative of some problem in the near future.
-> Error: this tells that due to more serious problem, the software has not been able to perform some function
->critical: this tells serious error, indicating that the program itself may be unale to continue running

we can create more levels, each level is assigned a value
        level   |   numeric value
        NOTSET  |   0
        DEBUG   |   10
        INFO    |   20
        WARNING |   30
        ERROR   |   40
        CRITICAL|   50

by default the level above waring are printed we can change the default by setting basic configuration

"""
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s -%(levelname)s - %(message)s',datefmt='%m/%d/%y %H:%M:%S)')
logging.debug("this is a debug message")
logging.info("this is an info mesasage")
logging.warning("this is an warning message")
logging.error("this is an error message")
logging.critical("this is an critical mess age")

# we can create our own logger instead of root in helper.py file
import helper

#log handler: handler objects are used for dispatching the appropriate log message to handler  specific destination
logger=logging.getLogger(__name__)
#create handler
stream_h=logging.StreamHandler()
file_h=logging.FileHandler("file.log")

#level and the format
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter=logging.Formatter('%(name)s -(levelname)s -5(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning('this is a warning')
logger.error('this is the error')

