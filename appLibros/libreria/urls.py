from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.inicio,name="inicio"),
    path('nosotros',views.nosotros,name="nosotros"),
    path('libros',views.libros,name="libros"),
    path('libros/crear',views.crearLibro,name="crearLibro"),
    path('libros/editar/<int:id>',views.editarLibro,name="editarLibro"),
    path('libros/eliminar/<int:id>',views.eliminarLibro,name="eliminarLibro"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   