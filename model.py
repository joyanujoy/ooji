# -*- coding: utf-8 -*
import uuid
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Sequence, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.exc import IntegrityError

Base = declarative_base()


class Url(Base):
    """ Url class represents a URL

    Base Table
    ----------
    url

    Columns
    -------
    id : primary_key, UUID5 of Url
    url_text : full URL text e.g http://python.org
    """

    __tablename__ = 'url'

    id = Column(String(50), primary_key=True)
    url_text = Column(String(4000))

    def __init__(self, id, url_text):
        self.id = id
        self.url_text = url_text

    def __repr__(self):
        return "Url('{self.id}', '{self.url_text}')".format(self=self)


class Request(Base):
    """ Request class represents a shorten URL request

    Base Table
    ----------
    request

    Columns
    -------
    id : primary key
    url_id : foreign key to URL table
    """

    __tablename__ = 'request'

    id = Column(Integer, Sequence('request_id_seq'), primary_key=True)
    url_id = Column(String(50), ForeignKey('url.id'))

    url = relationship('Url', backref=backref('requests', order_by=id))

    def __init__(self, url_id):
        self.url_id = url_id

    def __repr__(self):
        return "Request('{self.url_id}')".format(self=self)


class Model(object):
    """ Provides methods for database operations

    Attributes
    ----------
    dbl = Database Url in the format driver://user:pwd@host:port/dbname
    engine = SQLAlchemy engine
    session = SQLAlcheemy session
    """

    def __init__(self, driver='postgresql', usr='ajoy', pwd='ajoy',
                 host='localhost', port='5432', db='ajoy'):
        dbl = "{d}://{u}:{p}@{h}:{pt}/{db}"
        self.db = dbl.format(d=driver, u=usr, p=pwd, h=host, pt=port, db=db)
        self.engine = create_engine(self.db)

        Session = sessionmaker(bind=self.engine, autocommit=False)
        self.session = Session()

    def add_url(self, url):
        """
        Takes a url, creates a record in database and returns the record id

        Parameters
        ----------
        url : URL encoded String e.g http://www.example.com/d%C3%BCsseldorf?neighbourhood=L%C3%B6rick

                Input URL needs to be url encoded because SHA encoder doesn't
                accept utf8

        Returns
        -------
        id : Integer, record id from database
        """

        uid = str(uuid.uuid5(uuid.NAMESPACE_URL, url))
        url_obj = Url(uid, url)

        try:
            self.session.add(url_obj)
            self.session.commit()
        except IntegrityError:
            self.session.rollback()  # ie url is already in url table, ignore
        except:
            self.session.rollback()
            raise

        req_obj = Request(uid)

        try:
            self.session.add(req_obj)
            self.session.commit()
        except:
            raise

        id = req_obj.id

        try:
            self.session.expunge(url_obj)
            self.session.expunge(req_obj)
        except:
            pass

        return id

    def query_url(self, url_id):
        """
        Queries for url_id in database and returns url_Text

        Parameters
        ----------
        url_id : Integer id of the URL

        Returns
        -------
        url_text : URL as urlencoded String, from Url table
        """
        try:
            url = (
                self.session.query(Url.url_text)
                .join(Request)
                .filter_by(id=url_id)
                .scalar()
            )

        except:
            raise

        return url
