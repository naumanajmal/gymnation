from datetime import datetime
from typing import List

class MembershipService:
    def validate_membership(self, member):
        if member.status != 'Active':
            raise ValueError("Membership is not active.")
        if member.expiry_date < datetime.now().date():
            raise ValueError("Membership has expired.")
        return True

class CheckInService:
    def process_check_in(self, member, location, session_type):
        service = MembershipService()
        service.validate_membership(member)
        # Logic to save check-in
        return {"status": "success", "message": "Check-in processed."}

class TrainerAssignmentService:
    def assign_trainer(self, trainer, member):
        if len(trainer.assigned_members) >= 10:  # Example rule
            raise ValueError("Trainer cannot handle more than 10 members.")
        trainer.assigned_members.add(member)
        trainer.save()
        return {"status": "success", "message": "Trainer assigned."}

class AuditLogger:
    @staticmethod
    def log_change(action, details):
        # Simplified example, should ideally write to a database or a file
        print(f"{datetime.now()} - {action}: {details}")
