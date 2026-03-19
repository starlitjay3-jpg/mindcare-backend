import uuid
from sqlalchemy import Column, String, Boolean, Integer, Float, Text, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from app.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String(255), unique=True)
    hashed_password = Column(String(255))
    name = Column(String(100))
    role = Column(String(20), default="client")
    ai_credits = Column(Integer, default=3)
    is_active = Column(Boolean, default=True)

class Counselor(Base):
    __tablename__ = "counselors"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    specialty = Column(Text)

class BoardPost(Base):
    __tablename__ = "board_posts"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    title_encrypted = Column(Text)
    content_encrypted = Column(Text)

class Booking(Base):
    __tablename__ = "bookings"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    client_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    status = Column(String(50), default="pending")

class Payment(Base):
    __tablename__ = "payments"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    amount = Column(Float)

class AiChatSession(Base):
    __tablename__ = "ai_chat_sessions"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))

class AiChatMessage(Base):
    __tablename__ = "ai_chat_messages"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    session_id = Column(UUID(as_uuid=True), ForeignKey("ai_chat_sessions.id"))
    role = Column(String(20))
    content = Column(Text)

class AiCreditsLog(Base):
    __tablename__ = "ai_credits_log"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    change_amount = Column(Integer)