from django.urls import path
from .views import home, libro_lista, form_libro

urlpatterns = [
    path('', home, name="home"),
    path('libro-lista', libro_lista, name="libro_lista"),
    path('form-libro', form_libro, name="form_libro"),
]
