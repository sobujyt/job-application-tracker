from django.db import models


class JobApplication(models.Model):
    APPLIED = "Applied"
    INTERVIEW = "Interview"
    OFFER = "Offer"
    ACCEPTED = "Accepted"
    REJECTED = "Rejected"

    STATUS_CHOICES = [
        (APPLIED, "Applied"),
        (INTERVIEW, "Interview"),
        (OFFER, "Offer"),
        (ACCEPTED, "Accepted"),
        (REJECTED, "Rejected"),
    ]

    company_name = models.CharField(max_length=150)
    position = models.CharField(max_length=150)
    job_location = models.CharField(max_length=150)
    salary = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default=APPLIED
    )
    application_date = models.DateField()
    deadline = models.DateField()
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.company_name} - {self.position}"
