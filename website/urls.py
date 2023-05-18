from django.urls import path 
from . import views
from .views import  (CustomerRecordView,
                    RecordDeleteView,
                    RecordAddView,
                    UpdateRecordView
                    )

urlpatterns = [
    path('', views.home, name='home'),
    # path('/login', views.login, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('register', views.register_user, name='register'),
    path('record/<int:pk>', CustomerRecordView.as_view(), name='record'),
    path('record/<int:pk>/delete', RecordDeleteView.as_view(), name='delete_record'),
    path('record/add_record', RecordAddView.as_view(), name='add_record'),
    path('update_record/<int:pk>', UpdateRecordView.as_view(), name='update_record'),
    path('privacy', views.PrivacyView, name='privacy'),
    path('about_us', views.AboutView, name='about'),
    path('contact_page', views.ContactView, name='contact'),







]