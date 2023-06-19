from django.shortcuts import render
from .models import Reality

# Create your views here.

def reality_view(request):
    realities = Reality.objects.all()
    return render(request, template_name='reality_template.html',context={"realities": realities})
