from django.contrib import admin
from django.urls import path
from api_app.views import drink_list, drink_detail
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('drinks/',drink_list,name="drinks"),
    path('drinks/<int:id>',drink_detail,name="drink"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
