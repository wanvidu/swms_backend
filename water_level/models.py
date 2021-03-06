from django.db import models
from month.models import MonthField


class WaterLevel(models.Model):
    id = models.AutoField(primary_key=True)
    reservoir = models.ForeignKey(
        "reservoirs.Reservoir", on_delete=models.CASCADE)
    date = MonthField("Month Value", help_text="Month Value")
    water_level = models.IntegerField()
    rainfall = models.IntegerField()
    temperature = models.IntegerField()
    evaporation = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["reservoir", "date"]
        unique_together = ['reservoir', 'date']

    def __str__(self):
        return 'Water Level : ' + self.reservoir.name + ", " + str(self.date)
