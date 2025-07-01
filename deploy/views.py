from django.shortcuts import render, redirect
from django.views import View

class Forside(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'deploy/forside.html')
    
class Ind(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'deploy/ind.html')
    
class Punkt1(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'deploy/punkt1.html')
    
class Punkt2(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'deploy/punkt2.html')
    
class Punkt3(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'deploy/punkt3.html')
    
class Punkt4(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'deploy/punkt4.html')
    
class Punkt5(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'deploy/punkt5.html')
    
class Punkt6(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'deploy/punkt6.html')
    
class Punkt7(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'deploy/punkt7.html')
    
class Punkt8(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'deploy/punkt8.html')
    
class Punkt9(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'deploy/punkt9.html')
    
class Punkt10(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'deploy/punkt10.html')