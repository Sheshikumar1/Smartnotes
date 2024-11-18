from django.shortcuts import render,get_object_or_404
from django.http import Http404,HttpResponseRedirect
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from .models import Notes
from .forms import NotesForm
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


class NotesUpdateView(UpdateView):  # Updated view name to match URL and class name convention
    model = Notes
    form_class = NotesForm
    template_name = 'notes/notes_form.html'
    success_url ='/smart/notes'

    def get_object(self, queryset=None):
        # Fetch the note belonging to the logged-in user with a specific pk
        obj = get_object_or_404(Notes, pk=self.kwargs['pk'], user=self.request.user)
        print("Updating note with ID:", obj.pk)  # Debugging line to verify instance
        return obj

    # Temporarily comment out `form_valid` to let `UpdateView` handle saving by default
    # def form_valid(self, form):
    #     form.instance = self.get_object()
    #     return super().form_valid(form)

   

class NotesCreateView(CreateView):
    model = Notes
    form_class = NotesForm
    
    success_url ='/smart/notes'
    login_url='/admin'

    def form_valid(self, form):
        # Create a note instance without saving it yet
        note = form.save(commit=False)
        note.user = self.request.user  # Set the current logged-in user
        note.save()  # Now save it to the database
        return HttpResponseRedirect(self.success_url)
    
class NotesListView(LoginRequiredMixin,ListView):
    model = Notes
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'
    login_url="/admin"

    def get_queryset(self):
        return self.request.user.notes.all()

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'
    template_name = 'notes/notes_details.html'

class NotesDeleteView(DeleteView):
    model=Notes
    success_url='/smart/notes'
    template_name='notes/notes_delete.html'