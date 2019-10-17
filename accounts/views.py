from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from .models import Profile

#create a SignUpView
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name= 'accounts/signup.html'


class ProfileCreateView(generic.CreateView):
    model = Profile
    template_name = 'profile_create.html'
    success_url = reverse_lazy('chats:chat_list')
    fields = ('bio', 'location', 'avatar',)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProfileDetailView(generic.DetailView):
    model = Profile
    template_name = 'profile_detail.html'
