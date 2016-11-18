import MySQLdb

class Connection:
    def __init__(self, user, password, db, host='localhost'):
        self.user = user
        self.host = host
        self.password = password
        self.db = db
        self._connection = None

    @property
    def connection(self):
        return self._connection

    def __enter__(self):
        self.connect()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()

    def connect(self):
        if not self._connection:
            self._connection = MySQLdb.connect(
                host=self.host,
                user=self.user,
                passwd=self.password,
                db=self.db,
                charset='utf8',
                use_unicode=True

            )

    def disconnect(self):
        if self._connection:
            self._connection.close()


class Computer:
    def __init__(self, db_connection, brand, price, processor_type, screen_size):
        self.db_connection = db_connection.connection
        self.brand = brand # производитель
#        self.type = type  # desktops, laptop, tablet
        self.screen_size = screen_size
#        self.installed_OS = installed_OS
        self.processor_type = processor_type
#        self.RAM = RAM
        self.price = price

    def save(self):
        c = self.db_connection.cursor()
        c.execute('INSERT INTO my_lab6_computermodel (brand, price, processor_type, screen_size) VALUES (%s, %s, %s, %s)',
                  (self.brand, self.price, self.processor_type, self.screen_size))
        self.db_connection.commit()
        c.close()

    def update(self):
        c = self.db_connection.cursor()
        #self.price = '20 руб'
        c.execute('UPDATE my_lab6_computermodel SET price = "0" WHERE id=2')
        self.db_connection.commit()
        c.close()

    def delete_item(self):
        c=self.db_connection.cursor()
        c.execute('DELETE FROM my_lab6_computermodel WHERE id=1')
        self.db_connection.commit()
        c.close()

con = Connection('dbuser', '123', 'shop_db')

with con:
    computer = Computer(con, 'Asus', '40000 руб', 'Inspiron', 10.0)
    computer.save()
    computer.delete_item()
    computer.update()