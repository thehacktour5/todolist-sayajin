from rest_framework.routers import DefaultRouter

from app.todolist.views import ItemViewSet

router = DefaultRouter()

router.register('item/', ItemViewSet, basename='user')

urlpatterns = router.urls