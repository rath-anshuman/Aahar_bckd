from django.shortcuts import render
from account.models import Visitor


# def abc(request):
#     visitors = Visitor.objects.all().order_by('-day')
#     return render(request, 'a.html', {'visitors': visitors})


def fetch_visitors(request):
    visitors = Visitor.objects.all().order_by('-day')
    return render(request, 'partials/visitors_table.html', {'visitors': visitors})


def abc(request):
    return render(request, 'a.html')
