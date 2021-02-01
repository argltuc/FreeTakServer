#######################################################
# 
# serverdestination.py
# Python implementation of the Class serverdestination
# Generated by Enterprise Architect
# Created on:      28-Sep-2020 10:48:18 PM
# Original author: natha
# 
#######################################################
from sqlalchemy import Column, ForeignKey
from FreeTAKServer.model.SQLAlchemy.Root import Base
from sqlalchemy import String
from sqlalchemy.orm import relationship


class Serverdestination(Base):
# default constructor  def __init__(self):  
    __tablename__ = "Serverdestination"
    PrimaryKey = Column(ForeignKey("Detail.PrimaryKey"), primary_key=True)
    Detail = relationship("Detail", back_populates="serverdestination")
    # string composed by IP:port: protocol:machineID.
    # <i> e.g. 192.168.0.103:4242:tcp:ANDROID-R52JB0CDC4E</i>
    destinations = Column(String)