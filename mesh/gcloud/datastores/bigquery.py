import mesh.base
from mesh.exceptions import *
from google.cloud import bigquery
import pandas as pd
import logging
log = logging.getLogger(__name__)


class BqConnect(mesh.base.Connection):
    """
    A simple wrapper of the authentication process for ease of use
    """
    def __init__(self):
        super(BqConnect, self).__init__()
        self.connection = None

    def from_file(self, json_file=None):
        self.connection = bigquery.Client.from_service_account_json(json_file)


class BigQuery(mesh.base.Data):
    """
    A class that thinly wraps functionlity in google's wonderful api, but in such a
    way that makes it consistent across various other tools and platforms.
    """
    def __init__(self, connection: BqConnect):
        """
        :param connection:
        """
        self.connection = connection.connection
        super(BigQuery, self).__init__()

    # todo make this more spark-like
    @staticmethod
    def _limit_read(limit_sql, limit_percentage):
        """
        :param limit_sql:
        :param limit_percentage:
        :return:
        """
        return ' WHERE MOD({},10) < {}'.format(limit_sql, limit_percentage)

    @staticmethod
    def sql_builder(project=None, db=None, tbl=None, sql=None,
                    limit_sql=None, limit_percentage=2):
        """
        :param project:
        :param db:
        :param tbl:
        :param sql:
        :param limit_sql:
        :param limit_percentage:
        :return:
        """
        suffix = ''
        if limit_sql:
            suffix = BigQuery._limit_read(limit_sql, limit_percentage)

        if not (tbl or sql):
            raise InvalidData('no table name or features provided')
        elif tbl:
            return 'SELECT * FROM `{}.{}.{}` {}'.format(project, db, tbl, suffix)
        elif sql:
            return '{} {}'.format(sql, suffix)

    def read(self, sql=None, limit_sql=None, limit_percentage=1):
        if limit_sql:
            sql = BigQuery.sql_builder(sql=sql, limit_sql=limit_sql, limit_percentage=limit_percentage)
        self.data = self.connection.query(sql)
        return self

    def to_panda(self, *args, **kwargs) -> pd.DataFrame:
        """
        return a pandas dataframe from a bigquery frame
        :param args:
        :param kwargs:
        :return:
        """
        return self.data.to_dataframe()




