from django.urls import path


from . import views

app_name = 'chats'

urlpatterns = [
    path('<int:pk>/comment/', views.add_comment_to_chat, name='add_comment_to_chat'),
    path('<int:pk>/comment/remove', views.CommentDeleteView.as_view(), name='delete_comment'),
    path('<int:pk>/comment/update/', views.CommentUpdateView.as_view(), name='update_comment'),
    path('<int:pk>/comment/new/', views.CommentCreateView.as_view(), name='add_comment'),
    path('<int:pk>/', views.ChatDetailView.as_view(), name='chat_detail'),
    path('', views.ChatListView.as_view(), name='chat_list'),
]

#chat_detail is stating the primary key of that certain chat detail
#chat_list is the default path
