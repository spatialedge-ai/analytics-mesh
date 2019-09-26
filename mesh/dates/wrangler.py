import logging
from datetime import datetime

log = logging.getLogger(__name__)


def date_formatter(string_date, day):
    """
    The day modifier is optional, if a complete string date is provided then simply return
    the object to that date, and ignore the day_mod
    :param string_date: a string date of YYYYMMDD or YYYYMM. The former overrides the day parameter (causes
    it to be ignored), but YYYYMM appends day
    :return:
    """
    format = '%Y%m%d'
    if len(string_date) == 8:
        log.warning('a specific date has been specified')
        return datetime.strptime(string_date, format)
    else:
        log.debug('modifying/augmenting the date with the correct run day')
        if len(string_date) != 6:
            raise ValueError('expected YYYYMM format as day modifier is to be applied')
        else:
            if isinstance(day, int):
                day = '{:02d}'.format(day)
            return datetime.strptime('{yyyymm}{dd}'.format(yyyymm=string_date, dd=day), format)
