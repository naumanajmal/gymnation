from django.shortcuts import render, get_object_or_404
from .models import Member, Trainer, CheckIn, MembershipPlan

def member_profile(request):
    member = get_object_or_404(Member, id=2)
    check_ins = CheckIn.objects.filter(member=member)
    return render(request, "member_profile.html", {"member": member, "check_ins": check_ins})
