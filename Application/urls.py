from django.conf.urls import url
from django.urls import path
from . import views
app_name='Application'
urlpatterns=[
        path('visitor/',views.add_visitor,name='Visitor_Add'),
            path('name-autocomplete/',views.HostAutocomplete.as_view(),name='name-autocomplete'),

]