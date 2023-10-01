from .Logger import Logger
from datetime import datetime


def debugger(func):
    def wrapper(*args, **kwargs):
        try:
            # start time
            now = datetime.now()
            
            # enable logging
            Logger.log()
            Logger.debug(f'Executing {func.__name__}')

            # execute function
            res = func(*args, **kwargs)

            # end time
            Logger.debug(f'Finished executing {func.__name__}')
            Logger.info(f'Total time: {datetime.now() - now}')

            # disable logging
            Logger.log()
            return res
        except Exception as e:
            Logger.error(f'Error executing {func.__name__}. error: {e}')
            Logger.log()
            return None
    return wrapper