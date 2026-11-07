
from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime,
    ForeignKey
)
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from database import Base


# 1. Task Management Table
class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    assigned_to = Column(String(100), nullable=False)
    status = Column(String(30), default="Pending")
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )


# 2. Candidate Management / ATS Table
class Candidate(Base):
    __tablename__ = "candidates"

    id = Column(Integer, primary_key=True, index=True)
    candidate_name = Column(String(100), nullable=False)

    email = Column(
        String(150),
        unique=True,
        nullable=False,
        index=True
    )

    phone = Column(String(20), nullable=True)
    position = Column(String(100), nullable=False)
    experience = Column(Integer, default=0)
    status = Column(String(30), default="Applied")
    resume_link = Column(String(500), nullable=True)
    notes = Column(Text, nullable=True)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    # One candidate can have multiple interviews
    interviews = relationship(
        "Interview",
        back_populates="candidate"
    )


# 3. Interview Scheduling Table
class Interview(Base):
    __tablename__ = "interviews"

    id = Column(Integer, primary_key=True, index=True)

    # Link interview to a candidate
    candidate_id = Column(
        Integer,
        ForeignKey("candidates.id"),
        nullable=True,
        index=True
    )

    # Keep these fields for compatibility with existing APIs
    candidate_name = Column(String(100), nullable=False)
    candidate_email = Column(String(150), nullable=False)

    interview_date = Column(DateTime, nullable=False)
    interview_mode = Column(String(20), nullable=False)
    status = Column(String(30), default="Scheduled")

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    candidate = relationship(
        "Candidate",
        back_populates="interviews"
    )
