from django.core.urlresolvers import reverse, reverse_lazy
from django.http import Http404
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import UpdateView
from django.views.generic import ListView

from braces.views import LoginRequiredMixin

from .models import Device
from .forms import DeviceUpdateForm, DeviceCreateForm


class DeviceListView(LoginRequiredMixin, ListView):
    model = Device

    def get_queryset(self):
        return Device.objects.filter(owner=self.request.user)


class DeviceDetailView(LoginRequiredMixin, DetailView):
    model = Device

    def get_queryset(self):
        return Device.objects.filter(owner=self.request.user)


class DeviceUpdateView(LoginRequiredMixin, UpdateView):
    form_class = DeviceUpdateForm
    model = Device


    # send the user back to the device page after a successful update
    def get_success_url(self):
        return reverse("devices:detail",
                       kwargs={"pk": self.object.pk})

    def get_queryset(self):
        return Device.objects.filter(owner=self.request.user)


class DeviceDeleteView(LoginRequiredMixin, DeleteView):
    model = Device
    success_url = reverse_lazy('devices:list')


class DeviceCreateView(LoginRequiredMixin, CreateView):
    form_class = DeviceUpdateForm
    model = Device
    success_url = reverse_lazy('devices:list')
    template_name_suffix = "_create_form"

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(DeviceCreateView, self).form_valid(form)
