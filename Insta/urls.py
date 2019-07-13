from django.urls import path

from Insta.views import PostView, PostDetail

urlpatterns = [
    path("", PostView.as_view(), name="home"),
    path("post/<int:pk>/", PostDetail.as_view(), name="post_detail")

]
