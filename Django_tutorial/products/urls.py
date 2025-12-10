from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static





urlpatterns = [
    path('mugs/',views.index,name='home'),
    path('about/',views.about,name='about'),


    path('signup/',views.signup, name='signup'),
    path('',views.loginpage,name='login'),
    path('logout/', views.logout, name='logout'),

    path('bookhome/',views.book, name='book'),
    path('add/',views.add_book,name='add_book'),

    path('Editbook/<int:pk>/', views.Editbook, name='Editbook'),  # ✅ fixed
    path('Deletebook/<int:pk>/', views.Delete, name='Deletebook'),

    path('members/', views.members, name='members'),
    path('contacts/', views.contacts, name='contacts'),

    # path('test/<int:id>',views.test,name='test'),
    
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)