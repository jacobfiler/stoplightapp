from django.db import models

class ReformArea(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Reform(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    slcid = models.CharField(max_length=10, unique=True)
    criteria = models.TextField()
    reform_area = models.ForeignKey(ReformArea, on_delete=models.CASCADE, related_name='reforms')

    def __str__(self):
        return f"{self.name} ({self.slcid})"

class State(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

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

    def __str__(self):
        return f"{self.reform.name} in {self.state.name} - {self.get_status_display()}"