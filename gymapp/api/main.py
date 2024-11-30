import os
from django.conf import settings

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gym.settings')
import django
django.setup()

from fastapi import FastAPI, HTTPException
from gymapp.models import Member, CheckIn
from gymapp.schemas.models import Member as MemberSchema
from gymapp.schemas.models import CheckIn as CheckInSchema
app = FastAPI()

@app.post("/members/")
async def register_member(member: MemberSchema):
    # Validate and register member in Django
    try:
        new_member = Member.objects.create(
            name=member.name, email=member.email, membership_type=member.membership_type
        )
        return {"success": True, "member_id": new_member.id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    


@app.post("/check-ins/")
async def process_check_in(check_in: CheckInSchema):
    # Validate and register member in Django
    try:
        new_check_in = CheckIn.objects.create(
            name=check_in.name, email=check_in.email, membership_type=check_in.membership_type
        )
        return {"success": True, "new_check_in_id": new_check_in.id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    