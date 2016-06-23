from django.views import generic
from .models import UserProfile, Product_Info
from django.contrib.auth.models import User

class UserProfileView(generic.DetailView):
    model = User
    template_name = 'registration/detail.html'
    context_object_name = 'user_object'
    def get_object(self):
        return User.objects.get(pk=self.request.user.id)

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        context['product'] = Product_Info.objects.filter(created_by = self.request.user)
        return context

class ProfileFormView(generic.UpdateView):
    model = UserProfile
    fields = ['location', 'gender', 'profile_picture']
    template_name = 'registration/userprofile_form.html'
    success_url = '/accounts/profile/'

    def get_object(self):
        return self.request.user.profile
