import re
import time

from sqlalchemy import (TIMESTAMP, Column, ForeignKey, Integer, String,
                        create_engine, event, func)
from sqlalchemy.ext.declarative import (AbstractConcreteBase, as_declarative,
                                        declared_attr)
from sqlalchemy.orm import relationship, scoped_session, sessionmaker

engine = create_engine("sqlite:///test.db", convert_unicode=True, echo=False)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = scoped_session(Session)


@event.listens_for(session.bind, "before_cursor_execute")
def before_cursor_execute(conn, cursor, statement, parameters, context, executemany):
    conn.info.setdefault("query_start_time", []).append(time.time())
    print("Start Query: %s" % statement)


@event.listens_for(session.bind, "after_cursor_execute")
def after_cursor_execute(conn, cursor, statement, parameters, context, executemany):
    total = time.time() - conn.info["query_start_time"].pop(-1)
    print("Query Complete!")
    print("Total Time: %f" % total)


@as_declarative()
class Base(object):
    @declared_attr
    def __tablename__(cls):
        cls_name = cls.__name__.lower()
        if cls_name.endswith("event"):
            return "{}_events".format(cls_name[: len(cls_name) - 5])
        else:
            return (
                "_".join(
                    map(lambda x: x.lower(), re.findall("[A-Z][^A-Z]*", cls.__name__))
                )
                + "s"
            )

    id = Column(Integer, primary_key=True)
    created_date = Column(
        TIMESTAMP, nullable=False, server_default=func.current_timestamp()
    )
    updated_date = Column(
        TIMESTAMP,
        nullable=False,
        server_default=func.current_timestamp(),
        onupdate=func.current_timestamp(),
    )


class _Event(AbstractConcreteBase):
    @declared_attr
    def hackinfo_id(self):
        return Column(ForeignKey("hackinfos.id", ondelete="CASCADE"))

    @declared_attr
    def hackinfo(self):
        return relationship("HackInfo")


class HackInfo(Base):
    __tablename__ = "hackinfos"

    url = Column(String(255), nullable=False)


class KeywordEvent(Base, _Event):
    keyword = Column(String(20), nullable=False)


if __name__ == "__main__":
    from sqlalchemy.orm import (contains_eager, eagerload, joinedload,
                                lazyload, subqueryload)

    Base.metadata.create_all(bind=engine)
    for i in range(1000):
        session.add(KeywordEvent(hackinfo=HackInfo(url="xxxxxx"), keyword="fsf"))
    session.commit()
    # session.query(KeywordEvent).options(joinedload(KeywordEvent.hackinfo)).all()
    """
    SELECT keyword_events.id AS keyword_events_id, keyword_events.created_date AS keyword_events_created_date, keyword_events.updated_date AS keyword_events_updated_date, keyword_events.keyword AS keyword_events_keyword, keyword_events.hackinfo_id AS keyword_events_hackinfo_id, hackinfos_1.id AS hackinfos_1_id, hackinfos_1.created_date AS hackinfos_1_created_date, hackinfos_1.updated_date AS hackinfos_1_updated_date, hackinfos_1.url AS hackinfos_1_url
FROM keyword_events LEFT OUTER JOIN hackinfos AS hackinfos_1 ON hackinfos_1.id = keyword_events.hackinfo_id
    Total Time: 0.000127
    """
    # session.query(KeywordEvent).options(eagerload(KeywordEvent.hackinfo)).all()
    """
    SELECT keyword_events.id AS keyword_events_id, keyword_events.created_date AS keyword_events_created_date, keyword_events.updated_date AS keyword_events_updated_date, keyword_events.keyword AS keyword_events_keyword, keyword_events.hackinfo_id AS keyword_events_hackinfo_id, hackinfos_1.id AS hackinfos_1_id, hackinfos_1.created_date AS hackinfos_1_created_date, hackinfos_1.updated_date AS hackinfos_1_updated_date, hackinfos_1.url AS hackinfos_1_url
FROM keyword_events LEFT OUTER JOIN hackinfos AS hackinfos_1 ON hackinfos_1.id = keyword_events.hackinfo_id
    Total Time: 0.000927
    """
    # session.query(KeywordEvent).options(subqueryload(KeywordEvent.hackinfo)).all()
    """
    SELECT keyword_events.id AS keyword_events_id, keyword_events.created_date AS keyword_events_created_date, keyword_events.updated_date AS keyword_events_updated_date, keyword_events.keyword AS keyword_events_keyword, keyword_events.hackinfo_id AS keyword_events_hackinfo_id
FROM keyword_events
Query Complete!
Total Time: 0.000113
Start Query: SELECT hackinfos.id AS hackinfos_id, hackinfos.created_date AS hackinfos_created_date, hackinfos.updated_date AS hackinfos_updated_date, hackinfos.url AS hackinfos_url, anon_1.keyword_events_hackinfo_id AS anon_1_keyword_events_hackinfo_id
FROM (SELECT DISTINCT keyword_events.hackinfo_id AS keyword_events_hackinfo_id
FROM keyword_events) AS anon_1 JOIN hackinfos ON hackinfos.id = anon_1.keyword_events_hackinfo_id ORDER BY anon_1.keyword_events_hackinfo_id
Query Complete!
Total Time: 0.002664
    """
    # session.query(KeywordEvent).options(contains_eager(KeywordEvent.hackinfo)).all()
    """
    SELECT hackinfos.id AS hackinfos_id, hackinfos.created_date AS hackinfos_created_date, hackinfos.updated_date AS hackinfos_updated_date, hackinfos.url AS hackinfos_url, keyword_events.id AS keyword_events_id, keyword_events.created_date AS keyword_events_created_date, keyword_events.updated_date AS keyword_events_updated_date, keyword_events.keyword AS keyword_events_keyword, keyword_events.hackinfo_id AS keyword_events_hackinfo_id
FROM hackinfos, keyword_events
Query Complete!
Total Time: 0.000726
    """

    session.query(KeywordEvent).join(HackInfo).all()
    """
    SELECT keyword_events.id AS keyword_events_id, keyword_events.created_date AS keyword_events_created_date, keyword_events.updated_date AS keyword_events_updated_date, keyword_events.keyword AS keyword_events_keyword, keyword_events.hackinfo_id AS keyword_events_hackinfo_id
FROM keyword_events JOIN hackinfos ON hackinfos.id = keyword_events.hackinfo_id
Query Complete!
Total Time: 0.000521
    """
