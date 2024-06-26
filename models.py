from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import DbConnect


class User(DbConnect):
    # 해당 모델이 사용할 table 이름 지정
    __tablename__ = "users"

    # Model의 attribute(column) 생성 -> "="를 사용하여 속성을 정의
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    # 다른 테이블과의 관계 생성
    items = relationship("Item", back_populates="owner") # 부모 객체를 참조하는 참조 변수


class Item(DbConnect):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items") # 자식 객체들을 참조하는 참조 변수