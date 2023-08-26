from django.urls import path
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from .views import TasksView

router = routers.DefaultRouter()

router.register('tasks/api/v1', TasksView, 'tasks')

urlpatterns = router.urls

urlpatterns.append(path('docs/', include_docs_urls(title="Tasks API")))#Documentacion de la api utilizando 'coreapi'