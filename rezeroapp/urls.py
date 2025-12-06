from django.urls import path
from . import views

app_name = "rezeroapp"

# appのurls.pyをそれぞれ書く
urlpatterns = [
  path("", views.IndexView.as_view(), name="index"),
  path("rezero-detail/<int:pk>/",views.RezeroDetail.as_view(),name="rezero_detail"),

  path("anything-list/",views.AnythingView.as_view(),name="anything_list"),

  path("lastest-list/",views.LastestView.as_view(),name="lastest_list"),
  
  path("character-list/",views.CharacterView.as_view(),name="character_list"),

  path("contact/",views.ContactView.as_view(),name = "contact"),

  path("post/", views.PostView.as_view(), name="post"),

  path("post_done/", views.PostSuccessView.as_view(), name="post_done"),

]

