from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import JobApplicationForm
from .models import JobApplication


def home(request):
    applications = JobApplication.objects.all()
    total = applications.count()
    status_counts = {
        status_value: applications.filter(status=status_value).count()
        for status_value, _ in JobApplication.STATUS_CHOICES
    }
    context = {
        "total": total,
        "status_counts": status_counts,
    }
    return render(request, "home.html", context)


def job_list(request):
    applications = JobApplication.objects.all()
    return render(request, "jobs/list.html", {"applications": applications})


def job_detail(request, pk):
    application = get_object_or_404(JobApplication, pk=pk)
    return render(request, "jobs/detail.html", {"application": application})


def job_create(request):
    if request.method == "POST":
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Job application added successfully.")
            return redirect("job_list")
    else:
        form = JobApplicationForm()
    return render(request, "jobs/create.html", {"form": form})


def job_update(request, pk):
    application = get_object_or_404(JobApplication, pk=pk)
    if request.method == "POST":
        form = JobApplicationForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
            messages.success(request, "Job application updated successfully.")
            return redirect("job_list")
    else:
        form = JobApplicationForm(instance=application)
    return render(request, "jobs/update.html", {"form": form, "application": application})


def job_delete(request, pk):
    application = get_object_or_404(JobApplication, pk=pk)
    if request.method == "POST":
        application.delete()
        messages.success(request, "Job application deleted successfully.")
        return redirect("job_list")
    return render(request, "jobs/delete.html", {"application": application})
