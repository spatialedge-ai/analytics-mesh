from mesh.connectors.base import Connector
import psycopg2

class Postgres(Connector):

    def __init__(self):
        """
        A 'dumb' postgres writer that does a plain write (no columns added)
        """
        super().__init__()
        self.conn = None

    def connect(self, host, port, username, database, password):
        self.conn = psycopg2.connect("host={host} dbname={database} user={username} port={port} password={password}".format(
                username=username,
                host=host,
                port=port,
                database=database,
                password=password
            ))

    @staticmethod
    def _write_sql(table_name, data, append_str=None):
        """
        A helper method to format the string needed for inserting or updating via write
        """
        append_str = "" if not append_str else append_str
        return "INSERT INTO {table_name} ({column_list}) VALUES ({value_fmt_list})".format(
            table_name=table_name,
            column_list=','.join(data.keys()),
            value_fmt_list='%(' + ')s, %('.join(data.keys()) + ')s') + " {}".format(append_str)

    def write(self, table_name, data, upsert=False, upsert_keys=None):
        """
        A very simple write function that can insert or upsert a single row given a simple columnar constraint (provided in
        <upsert_key>
        :param table_name: a table in which to write
        :param data: a dictionary to write
        :param upsert: boolean to indicate if you wish to upsert
        :param upsert_keys: the constrained key which we wish to upsert on
        :return:
        """
        cur = self.conn.cursor()

        if upsert:
            # we are only dealing with the case where upsert_keys is a string
            upsert_keys = [upsert_keys] if isinstance(upsert_keys, str) else upsert_keys
            sql = self._write_sql(table_name, data,
                                  'ON CONFLICT ({upsert_key}) DO UPDATE SET {assignments};'.format(
                                      upsert_key=','.join(upsert_keys),
                                      assignments=", ".join(["{k} = excluded.{k}".format(k=k) for k, v in data.items()])

                                  ))
        else:
            sql = self._write_sql(table_name, data)

        cur.execute(sql, data)
        self.conn.commit()

    def read(self, table_name=None, project_list=None, limit=10, sql=None):
        """
        Very simple read wrapper that will execute raw sql or do a simple select of all or a projection of given
        what is provided
        :param table_name: a table_name (the table from which to read)
        :param project_list: a list of attributes to project against
        :param limit: how many records should be returned
        :param sql: raw sql override
        :return: as many records as specified in <limit>
        """
        cur = self.conn.cursor()
        if sql:
            cur.execute(sql)
        else:
            attributes = "*" if not project_list else ','.join(project_list)
            cur.execute('SELECT {attributes} FROM {table_name}'.format(
                attributes=attributes,
                table_name=table_name
            ))
        return cur.fetchmany(limit)
