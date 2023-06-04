from django.db import models

class Reja(models.Model):
    holatlar = (
        ("Yangi","Yangi"),
        ("Bajarilyapti","Bajarilyapti"),
        ("Bajarildi","Bajarildi")
    )
    sarlavha = models.CharField(max_length=150)
    tavsif = models.TextField()
    holat = models.CharField(max_length=20,choices=holatlar)
    vaqt = models.CharField(max_length=30)


    def __str__(self):
        return self.sarlavha