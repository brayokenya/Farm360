# accounts/views.py
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.utils import timezone
from datetime import datetime
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    DeleteView, 
    UpdateView
)
from .models import Event, Livestock



class IndexView(View):
    """
    View for the homepage.

    Attributes:
        template_name (str): HTML template for the homepage.
    """

    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        """
        Handle GET requests for the homepage.

        Args:
            request (HttpRequest): Django HttpRequest object.
            *args: Variable length argument list.
            **kwargs: Arbitrarily named arguments.

        Returns:
            HttpResponse: Rendered homepage.
        """
        return render(request, self.template_name)


class DashboardView(LoginRequiredMixin, View):
    """
    View for the user dashboard.

    Attributes:
        template_name (str): HTML template for the user dashboard.
    """

    template_name = "dashboard.html"

    def get(self, request, *args, **kwargs):
        """
        Handle GET requests for the user dashboard.

        Args:
            request (HttpRequest): Django HttpRequest object.
            *args: Variable length argument list.
            **kwargs: Arbitrarily named arguments.

        Returns:
            HttpResponse: Rendered user dashboard.
        """
        events = Event.objects.filter(user=request.user).order_by('-id')
        livestock = Livestock.objects.filter(user=request.user).order_by('-id')
        current_hour = timezone.localtime(timezone.now()).hour

        context = {
            'current_hour': current_hour,
            'event_list': events,
            'livestock_list': livestock,
        }

        return render(request, self.template_name, context)


class SignUpView(generic.CreateView):
    """
    View for user registration.

    Attributes:
        form_class (class): Django UserCreationForm for user registration.
        success_url (str): URL to redirect after successful registration.
        template_name (str): HTML template for user registration page.
    """

    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


@method_decorator(login_required, name="dispatch")
class ProfileView(View):
    """
    View for user profile.

    Attributes:
        template_name (str): HTML template for user profile page.
    """

    template_name = "profile.html"

    def get(self, request, *args, **kwargs):
        """
        Handle GET requests for user profile.

        Args:
            request (HttpRequest): Django HttpRequest object.
            *args: Variable length argument list.
            **kwargs: Arbitrarily named arguments.

        Returns:
            HttpResponse: Rendered user profile page.
        """
        return render(request, self.template_name)


class EventCreateView(LoginRequiredMixin, CreateView):
    """
    View for creating a new Event.

    Attributes:
        model (class): Django model class for Event.
        template_name (str): HTML template for the Event creation form.
        fields (list): List of fields to include in the form.
    """

    model = Event
    template_name = "event_form.html"
    fields = "__all__"

    def form_valid(self, form):
        """
        Validate the Event creation form.

        Args:
            form (Form): Django form instance.

        Returns:
            HttpResponse: Form validation result.
        """
        form.instance.user = self.request.user
        result = super().form_valid(form)
        messages.success(self.request, 'Event created successfully.')
        return result
    
    def form_invalid(self, form):
        """
        Handle cases where the Event creation form is invalid.

        Args:
            form (Form): Django form instance.

        Returns:
            HttpResponse: Form validation result.
        """
        return super().form_invalid(form)

    def get_success_url(self):
        """
        Get the URL to redirect after successful Event creation.

        Returns:
            str: URL for redirection.
        """
        return reverse_lazy("home")


class EventListView(LoginRequiredMixin, ListView):
    """
    View for displaying a list of Events.

    Attributes:
        model (class): Django model class for Event.
        template_name (str): HTML template for the list of Events.
    """

    model = Event
    template_name = "event_list.html"
    context_object_name = 'event_list'
    


    def get_queryset(self):
        """
        Get the queryset for the list of Events.

        Returns:
            QuerySet: List of Event objects.
        """
        return Event.objects.filter(user=self.request.user).order_by('-id')
   


class EventDetailView(DetailView):
    """
    View for displaying details of a Event.

    Attributes:
        model (class): Django model class for Event.
        template_name (str): HTML template for the Event details.
        context_object_name (str): Name of the context variable for the Event object.
    """

    model = Event
    template_name = "event_details.html"
    context_object_name = "event"

    def get_context_data(self, **kwargs):
        """
        Get additional context data for the Event details view.

        Args:
            **kwargs: Arbitrarily named arguments.

        Returns:
            dict: Additional context data.
        """
        context = super().get_context_data(**kwargs)
        context['event'] = self.object
        return context


class EventDeleteView(LoginRequiredMixin, DeleteView):
    """
    View for deleting a Event.

    Attributes:
        model (class): Django model class for Event.
        template_name (str): HTML template for the confirmation page.
    """

    model = Event
    template_name = "confirm_delete.html"  # Create a confirmation template

    def get_success_url(self):
        """
        Get the URL to redirect after successful Event deletion.

        Returns:
            str: URL for redirection.
        """
        messages.success(self.request, 'Event deleted successfully.')
        return reverse_lazy("home")


class EventUpdateView(LoginRequiredMixin, UpdateView):
    """
    View for updating a Event.

    Attributes:
        model (class): Django model class for Event.
        template_name (str): HTML template for the Event update form.
        fields (list): List of fields to include in the form.
    """

    model = Event
    template_name = "update_event.html"
    fields = "__all__"

    def form_valid(self, form):
        """
        Validate the Event update form.

        Args:
            form (Form): Django form instance.

        Returns:
            HttpResponse: Form validation result.
        """
        messages.success(self.request, 'Event updated successfully.')
        return super().form_valid(form)

    def get_success_url(self):
        """
        Get the URL to redirect after successful Event update.

        Returns:
            str: URL for redirection.
        """
        return reverse_lazy("home")


class LivestockCreateView(LoginRequiredMixin, CreateView):
    """
    View for creating a new Livestock record.

    Attributes:
        model (class): Django model class for Livestock.
        template_name (str): HTML template for the Livestock creation form.
        fields (list): List of fields to include in the form.
    """

    model = Livestock
    template_name = "livestock_form.html"
    fields = "__all__"

    def form_valid(self, form):
        """
        Validate the Livestock creation form.

        Args:
            form (Form): Django form instance.

        Returns:
            HttpResponse: Form validation result.
        """
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        """
        Get the URL to redirect after successful Livestock creation.

        Returns:
            str: URL for redirection.
        """
        return reverse_lazy("livestock_list")


class LivestockListView(LoginRequiredMixin, ListView):
    """
    View for displaying a list of Livestock records.

    Attributes:
        model (class): Django model class for Livestock.
        template_name (str): HTML template for the list of Livestock records.
        context_object_name (str): Name of the context variable for the Livestock list.
    """

    model = Livestock
    template_name = 'livestock_list.html'  
    context_object_name = 'livestock_list'

    def get_queryset(self):
        """
        Get the queryset for the list of Livestock records.

        Returns:
            QuerySet: List of Livestock objects.
        """
        # Filter the queryset based on the logged-in user
        return Livestock.objects.filter(user=self.request.user).order_by('-id')


class LivestockDetailView(DetailView):
    """
    View for displaying details of a Livestock record.

    Attributes:
        model (class): Django model class for Livestock.
        template_name (str): HTML template for the Livestock details.
        context_object_name (str): Name of the context variable for the Livestock object.
    """

    model = Livestock
    template_name = 'livestock_detail.html'
    context_object_name = 'livestock'




class LivestockUpdateView(LoginRequiredMixin, UpdateView):
    """
    View for updating a Livestock record.

    Attributes:
        model (class): Django model class for Livestock.
        template_name (str): HTML template for the Livestock update form.
        fields (list): List of fields to include in the form.
    """

    model = Livestock
    template_name = "livestock_form.html" 
    fields = "__all__"

    def form_valid(self, form):
        """
        Validate the Livestock update form.

        Args:
            form (Form): Django form instance.

        Returns:
            HttpResponse: Form validation result.
        """
        return super().form_valid(form)

    def get_success_url(self):
        """
        Get the URL to redirect after successful Livestock update.

        Returns:
            str: URL for redirection.
        """
        return reverse_lazy("livestock_detail", kwargs={"pk": self.object.pk})




class LivestockDeleteView(LoginRequiredMixin, DeleteView):
    """
    View for deleting a Livestock record.

    Attributes:
        model (class): Django model class for Livestock.
        template_name (str): HTML template for the confirmation page.
    """

    model = Livestock
    template_name = "confirm_delete.html"  

    def get_success_url(self):
        """
        Get the URL to redirect after successful Livestock deletion.

        Returns:
            str: URL for redirection.
        """
        return reverse_lazy("livestock_list")
