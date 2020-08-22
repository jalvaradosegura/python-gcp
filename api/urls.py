from django.urls import path

from .views import DrugList, DrugDetail, DrugPost, DrugPutDelete

urlpatterns = [
    path(
        route='drugs/',
        view=DrugList.as_view(),
    ),
    path(
        route='drugs/<int:id>/',
        view=DrugDetail.as_view(),
    ),
    path(
        route='drug/',
        view=DrugPost.as_view(),
    ),
    path(
        route='drug/<int:id>/',
        view=DrugPutDelete.as_view(),
    ),
]
