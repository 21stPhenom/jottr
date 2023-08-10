from django.urls import path
from notes import views
import notes

app_name = 'notes'

urlpatterns = [
    path('', views.index, name='index'),
    path('notes/', views.all_notes, name='all_notes'),
    path('add-note/', views.add_note, name='add_note'),
    path('<int:pk>/', views.view_note, name='view_note'),
    path('<int:pk>/update/', views.update_note, name='update_note'),
    path('<int:pk>/delete/', views.delete_note, name='delete_note'),
    path('<int:pk>/archive/', views.archive_note, name='archive_note'),
    path('notes/archives/', views.all_archives, name='all_archives')
]
