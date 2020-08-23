from django.urls import path

from .views import (
    DrugList,
    DrugDetail,
    DrugPost,
    DrugPutDelete,
    VaccinationListCreate,
    VaccinationDetailPutDelete,
    GetToken
)

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
    path(
        route='vaccination/',
        view=VaccinationListCreate.as_view(),
    ),
    path(
        route='vaccination/<int:id>/',
        view=VaccinationDetailPutDelete.as_view(),
    ),
    path(
        route='token/',
        view=GetToken.as_view(),
    ),
]
