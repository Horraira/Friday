from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('<int:year>/<str:month>/', views.home, name = 'home'),
    path('events', views.all_events, name = 'all-events'),
]

# path converters
# int: numbers
# str: strings
# path: whole urls /
# slug: hyphen-and_underchores_stuff
# UUID: you know