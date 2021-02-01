#######################################################
# 
# Summary.py
# Python implementation of the Class Summary
# Generated by Enterprise Architect
# Created on:      26-Sep-2020 9:41:46 PM
# Original author: natha
# 
#######################################################
from sqlalchemy import Column
from FreeTAKServer.model.SQLAlchemy.Root import Base
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Summary(Base):
# default constructor  def __init__(self):
    __tablename__ = "Summary"

    PrimaryKey = Column(ForeignKey("Detail.PrimaryKey"), primary_key=True)
    Detail = relationship("Detail", back_populates="summary")
    INTAG = Column(String)