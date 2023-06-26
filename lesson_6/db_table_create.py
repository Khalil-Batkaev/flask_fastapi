import sqlalchemy

__all__ = (
    'create_table',
    'create_tables',
)

DATABASE_URL = "sqlite:///mydatabase.db"


def create_table():
    metadata = sqlalchemy.MetaData()
    users = sqlalchemy.Table('users',
                             metadata,
                             sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
                             sqlalchemy.Column("username", sqlalchemy.String(32)),
                             sqlalchemy.Column("password", sqlalchemy.String(32)),
                             sqlalchemy.Column("first_name", sqlalchemy.String(128)),
                             sqlalchemy.Column("last_name", sqlalchemy.String(128)),
                             sqlalchemy.Column("birth_date", sqlalchemy.Date),
                             sqlalchemy.Column("email", sqlalchemy.String(128)),
                             sqlalchemy.Column("address", sqlalchemy.String(128)),
                             )
    tasks = sqlalchemy.Table('tasks',
                             metadata,
                             sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
                             sqlalchemy.Column("title", sqlalchemy.String(32)),
                             sqlalchemy.Column("description", sqlalchemy.String(256)),
                             sqlalchemy.Column("status", sqlalchemy.Boolean),
                             )
    engine = sqlalchemy.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
    metadata.create_all(engine)
    return users, tasks


def create_tables():
    metadata = sqlalchemy.MetaData()
    users = sqlalchemy.Table('users',
                             metadata,
                             sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
                             sqlalchemy.Column("first_name", sqlalchemy.String(128)),
                             sqlalchemy.Column("last_name", sqlalchemy.String(128)),
                             sqlalchemy.Column("email", sqlalchemy.String(128)),
                             sqlalchemy.Column("password", sqlalchemy.String(32)),
                             )
    goods = sqlalchemy.Table('goods',
                             metadata,
                             sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
                             sqlalchemy.Column("title", sqlalchemy.String(32)),
                             sqlalchemy.Column("description", sqlalchemy.String(256)),
                             sqlalchemy.Column("price", sqlalchemy.Float),
                             )
    orders = sqlalchemy.Table('orders',
                              metadata,
                              sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
                              sqlalchemy.Column("user_id",
                                                sqlalchemy.Integer,
                                                sqlalchemy.ForeignKey(users.c.id,
                                                                      ondelete='cascade',
                                                                      onupdate='cascade')),
                              sqlalchemy.Column("goods_id",
                                                sqlalchemy.Integer,
                                                sqlalchemy.ForeignKey(goods.c.id,
                                                                      ondelete='cascade',
                                                                      onupdate='cascade')),
                              sqlalchemy.Column("order_date", sqlalchemy.Date),
                              sqlalchemy.Column("status", sqlalchemy.String(32)),
                              )
    engine = sqlalchemy.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
    metadata.create_all(engine)
    return users, goods, orders
