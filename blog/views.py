from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Chat, Comment
from django.contrib.auth.decorators import login_required
# from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, DeleteView
# from .forms import ChatForm, CommentForm
#pass a get_queryset in listview to get back the objects filter by the chat name
class ChatListView(generic.ListView):
    model = Chat
    context_object_name = 'chat_list'
    template_name = '/blog/chat_list.html'

    # def get_queryset(self):
    #     return Chat.objects.filter(name=self.request.user)


class ChatDetailView(generic.DetailView):
    model = Chat


class CommentCreateView(LoginRequiredMixin, generic.CreateView):
    model = Comment
    fields = ('text',)
#where the login should be and where it will redirect you to
    login_url = '/login/'
    redirect_field_name = 'blog/chat_detail.html'
    # form_class = CommentForm


    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.chat_id = self.kwargs['pk']
        return super().form_valid(form)

class CommentUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Comment
    fields = ('text',)
#where the login should be and where it will redirect you to
    login_url = '/login/'
    # redirect_field_name = 'blog/chat_detail.html'
    # # form_class = CommentForm

class CommentDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Comment
    #it waits until you actually delete it to give you back success_url
    success_url = reverse_lazy('chat_list')


    #####################################################
    ######################################################

#decorator
# If the user is logged in, execute the view normally. The view code is free to assume the user is logged in.
@login_required
def add_comment_to_chat(request, pk):
    chat = get_object_or_404(Chat, pk=pk)
    #if some fillls in the form
    if request.method == 'POST':
        form = CommentForm(request,POST)
        #if they completed the form withou fail
        if form.is_valid():
            comment = form.save(commit=False)
            comment.chat = chat
            comment.save()
            return redirect('chat_detail', pk=chat.pk)
            #if know one fills out comment form
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {'form':form})
