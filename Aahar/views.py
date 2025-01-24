from django.shortcuts import render
from account.models import Visitor
from datetime import timedelta
from schdl.models import BHP

def fetch_visitors(request):
    visitors = Visitor.objects.all().order_by('-day')
    return render(request, 'partials/visitors_table.html', {'visitors': visitors})

def abc(request):
    updatedat = BHP.objects.get(id=1).updated_at
    updatedat_ist = updatedat + timedelta(hours=5, minutes=30)
    return render(request, 'home.html', {'updatedat': updatedat_ist})

