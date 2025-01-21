from django.shortcuts import render
from account.models import Visitor
def abc(request):
    visitors = Visitor.objects.all().order_by('-day')
    return render(request, 'a.html', {'visitors': visitors})