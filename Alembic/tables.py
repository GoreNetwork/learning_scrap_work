from sqlalchemy import (
    BigInteger,
    Column,
    DateTime,
    ForeignKey,
    Text,
    func,
)
from sqlalchemy.orm import declarative_base, relationship
Base = declarative_base()

# These are colums we want to use multiple times: any time this is inherited, these columns will be added
class TimestampMixin:
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

# Because we are inheriting from TimestampMixin, User table will have created_at and updated_at columns
class User(Base, TimestampMixin):
    __tablename__ = "users"
    telegram_id = Column(BigInteger, primary_key=True)
    full_name = Column(Text, nullable=False)
    username = Column(Text, nullable=True)
    language_code = Column(Text, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    referrer_id = Column(
        BigInteger,
        ForeignKey("users.telegram_id", ondelete="SET NULL"),
        nullable=True,
    )
    # self-referencing relationship
    referrer = relationship(
        "User",
        remote_side=[telegram_id],
        backref="referrals",
    )
