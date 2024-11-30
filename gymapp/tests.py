from django.db import models

class MembershipPlan(models.Model):
    name = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()  # in months
    access_levels = models.JSONField()  # Stores a list of access levels
    pricing_tier = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    membership_type = models.ForeignKey(MembershipPlan, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default="active")  # active, inactive, banned

    def __str__(self):
        return self.name

class Trainer(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    availability = models.JSONField()  # e.g., ['Monday', 'Wednesday']
    assigned_members = models.ManyToManyField(Member, related_name="trainers")

    def __str__(self):
        return self.name

class CheckIn(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=100)
    training_session_type = models.CharField(max_length=50)  # e.g., group, individual

    def __str__(self):
        return f"{self.member.name} - {self.timestamp}"
