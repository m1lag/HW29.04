from django.urls import path
from .views import NewsListView
from django.http import Http404

urlpatterns = [
    path('', NewsListView.as_view(), name='news_list'),

    path('<path:anything>/', lambda request, anything: (_ for _ in ()).throw(
        Http404("Сторінку в розділі Новини не знайдено")
    )),
]
