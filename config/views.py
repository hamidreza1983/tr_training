from django.shortcuts import render

def maintenance(req):
    return render(req, 'maintenance.html')