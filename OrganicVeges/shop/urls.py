from . import views
from django.urls import path
app_name='shop'
urlpatterns = [
    path('', views.Home, name='Home-page'),
    path('demo/', views.demo, name='shop_page'),
    path('checkout/', views.checkout, name='checkout_page'),
    path('viewDetail/<int:myid>', views.viewDetail, name='view-Detail'),
    path('AboutUs/', views.AboutUs, name='AboutUs'),
    path('ContactUs/', views.ContactUs, name='ContactUS'),
    path('postComment', views.postComment, name="postComment"),
    path('like/', views.like_post , name='like-post'),
    path('replyComment', views.replyComment, name="replyComment"),
]
