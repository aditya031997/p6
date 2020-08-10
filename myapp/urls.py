from django.urls import path
from myapp import views
app_name="myapp"

urlpatterns = [
    path('trail/',views.trail,name="trail"),
    path('about/',views.about,name="about"),
    path('download/',views.download,name="download"),
    path('document/',views.document,name="document"),
    path('get_demo/',views.get_demo,name="get_demo"),

]
