from django.urls import path
from .views import index, register, LoginView, product, message, MyView, dynamic, book_list, SignUpView, my_view
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', index, name='index'),
    path('register', register, name='register'),
    path('signup', SignUpView.as_view(), name='signup'),
    path('login', LoginView.as_view(next_page='product'), name='login'),
    # path('login', my_view, name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('product', product, name='product'),
    path('message', message, name='message'),
    path('index', MyView.as_view()),
    path('dynamic', dynamic, name='dynamic'),
    path('books', book_list, name='books'),
    path('password_reset', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete')
]