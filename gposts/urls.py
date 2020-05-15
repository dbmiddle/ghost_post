from django.urls import path

from gposts import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('upvote/<int:post_id>/', views.upvote_view),
    path('downvote/<int:post_id>/', views.downvote_view),
    path('boasts/', views.boasts),
    path('roasts/', views.roasts),
    path('addpost/', views.add_post),
    path('most_popular/', views.most_popular),
    path('least_popular/', views.least_popular)
]
