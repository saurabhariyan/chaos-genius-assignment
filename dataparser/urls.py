from django.urls import path
import dataparser.views as dp_views

urlpatterns = [
    path("dimensions/<str:filename>", dp_views.DimensionListView.as_view()),
    path("tree/<str:dataset>/<str:node>/", dp_views.TreeListView.as_view())
]
