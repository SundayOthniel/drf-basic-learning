from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('userList', userList.as_view({'get': 'list'}), name='userList'),
    # path('UserDetail/<int:id>', UserDetail.as_view(), name='UserDetail'),
    # path('snippets/<int:pk>/highlight/', SnippetHighlight.as_view()),
    # path('', api_root),
]
urlpatterns = format_suffix_patterns(urlpatterns)