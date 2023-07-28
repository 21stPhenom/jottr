from django.urls import path
from notes import views
import notes

app_name = 'notes'

urlpatterns = [
    path('', views.index, name='index'),
    path('notes/', views.all_notes, name='all_notes'),
    path('add-note/', views.add_note, name='add_note'),
    path('<str:short_title>/', views.view_note, name='view_note'),
    path('<str:short_title>/update/', views.update_note, name='update_note'),
    path('<str:short_title>/delete/', views.delete_note, name='delete_note')
]
handler_404 = notes.views.not_found
