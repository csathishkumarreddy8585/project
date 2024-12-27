from django.shortcuts import render

# Create your views here.


def Home(request):
    return render(request,'Home.html')

def Teams(request):
    return render(request,'Teams.html')


def Matches(request):
    return render(request,'Matches.html')

def Stats(request):
    return render(request,'Stats.html')


def point_table(request):
    return render(request,'point_table.html')

