import hashlib

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.utils.decorators import method_decorator
from notes.models import Note

def hash_title(string: str) -> str:
    pk = str(string).encode()

    hashed_title = hashlib.sha256(pk)
    return hashed_title.hexdigest()[0:13]

@method_decorator(login_required(login_url='authentication:login'), name='dispatch')
# Create your views here.
class IndexView(View):
    template_name = 'notes/index.html'
    
    def get(self, request, *args, **kwargs) -> HttpResponse:
        context = {
            'user': request.user if request.user.is_authenticated else None,
            'notes': Note.objects.filter(author=request.user)
        }
        return render(request, self.template_name, context=context)

@method_decorator(login_required(login_url='authentication:login'), name='dispatch')
class NotesView(View):
    manager = Note.objects
    template_name = 'notes/all_notes.html'

    def get(self, request, *args, **kwargs) -> HttpResponse:
        notes = self.manager.filter(author=request.user)
        context = {
            'notes': notes
        }
        return render(request, self.template_name, context=context)

@method_decorator(login_required(login_url='authentication:login'), name='dispatch')
class AddNote(View):
    manager = Note.objects
    template_name = 'notes/add_note.html'

    def get(self, request, *args, **kwargs) -> HttpResponse:
        context = {
            
        }
        return render(request, self.template_name, context=context)
    
    def post(self, request, *args, **kwargs) -> HttpResponse:
        note_title = request.POST['title']
        note_content = request.POST['content']

        new_note = Note.objects.create(
            author=request.user,
            title=note_title,
            content=note_content,
            short_title=hash_title(note_title),   
        )

        new_note.save()
        print(new_note.short_title)
        
        return redirect('notes:all_notes')

@method_decorator(login_required(login_url='authentication:login'), name='dispatch')
class ViewNote(View):
    manager = Note.objects
    template_name = 'notes/view_note.html'

    def get(self, request, short_title, *args, **kwargs) -> HttpResponse:
        note = get_object_or_404(self.manager, author=request.user, short_title=short_title)
        context = {
            'note': note
        }
        return render(request, self.template_name, context=context)

@method_decorator(login_required(login_url='authentication:login'), name='dispatch')
class UpdateNote(View):
    manager = Note.objects
    template_name = 'notes/update_note.html'

    def get(self, request, short_title, *args, **kwargs) -> HttpResponse:
        note = get_object_or_404(self.manager, author=request.user, short_title=short_title)
        context = {
            'note': note
        }
        return render(request, self.template_name, context=context)
    
    def post(self, request, short_title, *args, **kwargs) -> HttpResponse:
        note_title = request.POST['note_title']
        note_content = request.POST['note_content']

        note = get_object_or_404(self.manager, author=request.user, short_title=short_title)
        note.title = note_title
        note.content = note_content

        note.save(update_fields=['title', 'content'])
        return redirect('notes:view_note')
    
@method_decorator(login_required(login_url='authentication:login'), name='dispatch')
class DeleteNote(View):
    manager = Note.objects

    def get(self, request, short_title, *args, **kwargs) -> HttpResponse:
        note = get_object_or_404(self.manager, author=request.user, short_title=short_title)
        note.delete()
        return redirect('notes:all_notes')

class NotFoundView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'notes/error.html', {})
    

not_found = NotFoundView.as_view()
index = IndexView.as_view()
all_notes = NotesView.as_view()
add_note = AddNote.as_view()
view_note = ViewNote.as_view()
update_note = UpdateNote.as_view()
delete_note = DeleteNote.as_view()