from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class Member(BaseModel):
    id: int
    name: str
    email: str
    membership_type: str
    status: str = Field(default="active")  # active, inactive, banned

class Trainer(BaseModel):
    id: int
    name: str
    specialization: str
    availability: List[str]  # e.g., ['Monday', 'Wednesday']
    assigned_members: List[int] = []

class CheckIn(BaseModel):
    id: int
    member_id: int
    timestamp: datetime
    location: str
    training_session_type: str  # e.g., group, individual

class MembershipPlan(BaseModel):
    id: int
    name: str
    duration: int  # in months
    access_levels: List[str]
    pricing_tier: str  # e.g., basic, premium
