
from pydantic import BaseModel, EmailStr, ConfigDict, Field
from datetime import datetime
from typing import Optional, Literal


# ==========================
# TASK SCHEMAS
# ==========================

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    assigned_to: str


class TaskUpdate(BaseModel):
    status: Literal["Pending", "In Progress", "Completed"]


class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    assigned_to: str
    status: str
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


# ==========================
# INTERVIEW SCHEMAS
# ==========================

class InterviewCreate(BaseModel):
    candidate_id: Optional[int] = None
    candidate_name: str
    candidate_email: EmailStr
    interview_date: datetime
    interview_mode: Literal["Voice", "Video", "Chat"]


class InterviewResponse(BaseModel):
    id: int
    candidate_id: Optional[int] = None
    candidate_name: str
    candidate_email: EmailStr
    interview_date: datetime
    interview_mode: str
    status: str
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


# ==========================
# CANDIDATE / ATS SCHEMAS
# ==========================

class CandidateCreate(BaseModel):
    candidate_name: str = Field(min_length=2, max_length=100)
    email: EmailStr
    phone: Optional[str] = None
    position: str = Field(min_length=2, max_length=100)
    experience: int = Field(default=0, ge=0)
    resume_link: Optional[str] = None
    notes: Optional[str] = None


class CandidateUpdate(BaseModel):
    status: Literal[
        "Applied",
        "Shortlisted",
        "Interview Scheduled",
        "Selected",
        "Rejected"
    ]


class CandidateResponse(BaseModel):
    id: int
    candidate_name: str
    email: EmailStr
    phone: Optional[str] = None
    position: str
    experience: int
    status: str
    resume_link: Optional[str] = None
    notes: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)
