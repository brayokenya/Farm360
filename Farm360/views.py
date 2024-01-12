# accounts/views.py
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    DeleteView, 
    UpdateView
)
from .models import Collection, Sample
from .forms import SampleForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.utils import timezone
from datetime import datetime


class IndexView(View):
    
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    
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




class CollectionListView(LoginRequiredMixin, ListView):
    """
    View for displaying a list of collections.

    Attributes:
        model (class): Django model class for Collection.
        template_name (str): HTML template for the list of collections.
    """

    model = Collection
    template_name = "home.html"

    def get_queryset(self):
        """
        Get the queryset for the list of collections.

        Returns:
            QuerySet: List of Collection objects.
        """
        collections = Collection.objects.all()
        return collections

    def get_context_data(self, **kwargs):
        """
        Get additional context data for the template.

        Args:
            **kwargs: Arbitrarily named arguments.

        Returns:
            dict: Additional context data.
        """
        context = super().get_context_data(**kwargs)
        current_hour = timezone.localtime(timezone.now()).hour
        context['current_hour'] = current_hour
        return context



class CollectionDetailView(DetailView):
    """
    View for displaying details of a collection.

    Attributes:
        model (class): Django model class for Collection.
        template_name (str): HTML template for the collection details.
        context_object_name (str): Name of the context variable for the collection object.
    """

    model = Collection
    template_name = "collection_details.html"
    context_object_name = "collection"

    def get_context_data(self, **kwargs):
        """
        Get additional context data for the collection details view.

        Args:
            **kwargs: Arbitrarily named arguments.

        Returns:
            dict: Additional context data.
        """
        context = super().get_context_data(**kwargs)
        context["samples"] = Sample.objects.filter(collection=self.object)
        return context


class SampleCreateView(LoginRequiredMixin, CreateView):
    """
    View for creating a new sample.

    Attributes:
        model (class): Django model class for Sample.
        template_name (str): HTML template for the sample creation form.
        form_class (class): Django form class for the sample creation.
    """

    model = Sample
    template_name = "sample_form.html"
    form_class = SampleForm

    def form_valid(self, form):
        """
        Validate the sample creation form.

        Args:
            form (Form): Django form instance.

        Returns:
            HttpResponse: Form validation result.
        """
        form.instance.user = self.request.user
        form.instance.collection = Collection.objects.get(
            pk=self.kwargs["collection_id"]
        )
        messages.success(self.request, 'Sample created successfully.')
        return super().form_valid(form)

    def get_success_url(self):
        """
        Get the URL to redirect after successful sample creation.

        Returns:
            str: URL for redirection.
        """
        return reverse_lazy(
            "collection_details", kwargs={"pk": self.kwargs["collection_id"]}
        )


class CollectionCreateView(LoginRequiredMixin, CreateView):
    """
    View for creating a new collection.

    Attributes:
        model (class): Django model class for Collection.
        template_name (str): HTML template for the collection creation form.
        fields (list): List of fields to include in the form.
    """

    model = Collection
    template_name = "collection_form.html"
    fields = ["disease_term", "title"]

    def form_valid(self, form):
        """
        Validate the collection creation form.

        Args:
            form (Form): Django form instance.

        Returns:
            HttpResponse: Form validation result.
        """
        form.instance.user = self.request.user
        messages.success(self.request, 'Collection created successfully.')
        return super().form_valid(form)

    def get_success_url(self):
        """
        Get the URL to redirect after successful collection creation.

        Returns:
            str: URL for redirection.
        """
        return reverse_lazy("home")


class CollectionDeleteView(LoginRequiredMixin, DeleteView):
    """
    View for deleting a collection.

    Attributes:
        model (class): Django model class for Collection.
        template_name (str): HTML template for the confirmation page.
    """

    model = Collection
    template_name = "confirm_delete.html"  # Create a confirmation template

    def get_success_url(self):
        """
        Get the URL to redirect after successful collection deletion.

        Returns:
            str: URL for redirection.
        """
        messages.success(self.request, 'Collection deleted successfully.')
        return reverse_lazy("home")


class SampleDeleteView(LoginRequiredMixin, DeleteView):
    """
    View for deleting a sample.

    Attributes:
        model (class): Django model class for Sample.
        template_name (str): HTML template for the confirmation page.
    """

    model = Sample
    template_name = "confirm_delete.html"  # Create a confirmation template

    def get_success_url(self):
        """
        Get the URL to redirect after successful sample deletion.

        Returns:
            str: URL for redirection.
        """
        messages.success(self.request, 'Sample deleted successfully.')
        return reverse_lazy(
            "collection_details", kwargs={"pk": self.object.collection.id}
        )

    def delete(self, request, *args, **kwargs):
        """
        Handle the DELETE request and perform the sample deletion.

        Args:
            request (HttpRequest): Django HttpRequest object.
            *args: Variable length argument list.
            **kwargs: Arbitrarily named arguments.

        Returns:
            HttpResponse: Redirection after successful deletion.
        """
        self.object = self.get_object()
        collection_id = self.object.collection.id
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)


class CollectionUpdateView(LoginRequiredMixin, UpdateView):
    """
    View for updating a collection.

    Attributes:
        model (class): Django model class for Collection.
        template_name (str): HTML template for the collection update form.
        fields (list): List of fields to include in the form.
    """

    model = Collection
    template_name = "update_collection.html"
    fields = ["disease_term", "title"]

    def form_valid(self, form):
        """
        Validate the collection update form.

        Args:
            form (Form): Django form instance.

        Returns:
            HttpResponse: Form validation result.
        """
        messages.success(self.request, 'Collection updated successfully.')
        return super().form_valid(form)

    def get_success_url(self):
        """
        Get the URL to redirect after successful collection update.

        Returns:
            str: URL for redirection.
        """
        return reverse_lazy("home")


class SampleUpdateView(LoginRequiredMixin, UpdateView):
    """
    View for updating a sample.

    Attributes:
        model (class): Django model class for Sample.
        template_name (str): HTML template for the sample update form.
        form_class (class): Django form class for the sample update.
    """

    model = Sample
    template_name = "update_sample.html"
    form_class = SampleForm

    def form_valid(self, form):
        """
        Validate the sample update form.

        Args:
            form (Form): Django form instance.

        Returns:
            HttpResponse: Form validation result.
        """
        messages.success(self.request, 'Sample updated successfully.')
        return super().form_valid(form)

    def get_success_url(self):
        """
        Get the URL to redirect after successful sample update.

        Returns:
            str: URL for redirection.
        """
        return reverse_lazy(
            "collection_details", kwargs={"pk": self.object.collection.id}
        )
