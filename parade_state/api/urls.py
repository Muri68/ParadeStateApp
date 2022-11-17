from django.urls import path
from .views import ParadeStateListView, ParadeStateDetailView


urlpatterns = [
    path('', ParadeStateListView.as_view()),
    path('<int:id>/', ParadeStateDetailView.as_view()),
]