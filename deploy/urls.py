from django.urls import path
from . import views
from .views import Forside,Ind,Punkt1,Punkt2,Punkt3,Punkt4,Punkt5,Punkt6,Punkt7,Punkt8,Punkt9,Punkt10


urlpatterns = [
  path('', Forside.as_view(), name='forside'),
  path('ind', Ind.as_view(), name='ind'),
  path('punkt1', Punkt1.as_view(), name='punkt1'),
  path('punkt2', Punkt2.as_view(), name='punkt2'),
  path('punkt3', Punkt3.as_view(), name='punkt3'),
  path('punkt4', Punkt4.as_view(), name='punkt4'),
  path('punkt5', Punkt5.as_view(), name='punkt5'),
  path('punkt6', Punkt6.as_view(), name='punkt6'),
  path('punkt7', Punkt7.as_view(), name='punkt7'),
  path('punkt8', Punkt8.as_view(), name='punkt8'),
  path('punkt9', Punkt9.as_view(), name='punkt9'),
  path('punkt10', Punkt10.as_view(), name='punkt10'),
  
] 