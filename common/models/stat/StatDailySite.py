# coding: utf-8
from sqlalchemy import Column, Date, DateTime, Integer, Numeric
from sqlalchemy.schema import FetchedValue
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class StatDailySite(Base):
    __tablename__ = 'stat_daily_site'

    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False, index=True)
    total_pay_money = Column(Numeric(10, 2), nullable=False, server_default=FetchedValue())
    total_member_count = Column(Integer, nullable=False)
    total_new_member_count = Column(Integer, nullable=False)
    total_order_count = Column(Integer, nullable=False)
    total_shared_count = Column(Integer, nullable=False)
    updated_time = Column(DateTime, nullable=False, server_default=FetchedValue())
    created_time = Column(DateTime, nullable=False, server_default=FetchedValue())
