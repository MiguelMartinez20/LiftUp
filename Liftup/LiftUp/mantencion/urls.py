from django.conf.urls import url
from mantencion.views import TecnicoList, ClienteList, FormaTrabajoList
from django.urls import path
#from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('tecnico/', TecnicoList.as_view(), name='tecnicolist'),
    path('cliente/', ClienteList.as_view(), name='clientelist'),
    path('forma/', FormaTrabajoList.as_view(), name='formalist'),
] 