from django.urls import path
from . import views
from users import views as usr_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from .views import (PostListView,
                    PostDetailView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView,
                    UserPostListView)



urlpatterns = [
    path('', PostListView.as_view(template_name = 'blog/home.html'), name = 'blog-home'),
    path('post/<str:username>/', UserPostListView.as_view(template_name = 'blog/user_posts.html'), name = 'user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(template_name = 'blog/post_detail.html'), name = 'post-detail'),
    path('post/new/', PostCreateView.as_view(template_name = 'blog/post_create.html'), name = 'post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(template_name = 'blog/post_create.html'), name = 'post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(template_name = 'blog/post_delete.html'), name = 'post-delete'),
    path('about/',views.about, name = 'blog-about'),
    path('register/',usr_views.register, name = 'blog-register'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'), name = 'Login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'), name = 'Logout'),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name = 'password_reset'), #first page to request for password by email
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name = 'password_reset_done'),#after reset link has been sent for reset request, page that is displayed
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name = 'password_reset_confirm'),##third page that that provide the user with the actual reset interface
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name = 'password_reset_complete'),#last page to be displayed after password has been reset successuly
    path('profile/',usr_views.profile, name = 'profile'),

] 

if settings.DEBUG: #i.e if we are in debug mode
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



#<app>/<model>_<viewtype>.html

