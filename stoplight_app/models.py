from django.db import models
from simple_history.models import HistoricalRecords

class ReformArea(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Reform(models.Model):
    VERSION_CHOICES = [
        (1, 'Version 1'),
        (2, 'Version 2')
    ]

    slcid = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    reform_area = models.ForeignKey(ReformArea, on_delete=models.CASCADE, related_name='reforms')
    criteria = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True)
    version = models.PositiveSmallIntegerField(choices=VERSION_CHOICES, default=2)
    policy_specialist = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.slcid})"

class State(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class SourceType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Source(models.Model):
    reform_status = models.ForeignKey('ReformStatus', on_delete=models.CASCADE, related_name='sources')
    source_type = models.ForeignKey(SourceType, on_delete=models.CASCADE)
    url = models.URLField(max_length=500)

    def __str__(self):
        return f"{self.source_type.name} - {self.url}"

class ReformStatus(models.Model):
    class StatusChoices(models.TextChoices):
        RED = 'R', 'Red'
        YELLOW = 'Y', 'Yellow'
        GREEN = 'G', 'Green'
        BLUE = 'B', 'Blue'
        BLACK = 'K', 'Black'
        NULL = 'N', 'Null'

    reform = models.ForeignKey(Reform, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=1,
        choices=StatusChoices.choices,
        default=StatusChoices.NULL,
        blank=True, null=True
    )
    additional_notes = models.TextField(blank=True, null=True)
    win = models.BooleanField(default=False)
    citation = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    history = HistoricalRecords()

    def __str__(self):
        return f"{self.reform.name} in {self.state.name} - {self.get_status_display()}"
