from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def news_view(request):

    return HttpResponse('看这里')



