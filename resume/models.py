from django.db import models

class Education(models.Model):
    school = models.CharField(max_length=300)
    year = models.CharField(max_length=200)
    certificate = models.CharField(max_length=300)

    def __str__(self):
        return self.school


class Experience(models.Model):
    company = models.CharField(max_length=300)
    duration = models.CharField(max_length=300)
    role = models.CharField(max_length=300)
    responsibilities = models.CharField(max_length=300)


    def __str__(self):
        return self.role


class Percent(models.Model):
    percent = models.CharField(max_length=100)

    def __str__(self):
        return self.percent


class Skills(models.Model):
    skill = models.CharField(max_length=250)
    skill_percent = models.ForeignKey(Percent, on_delete=models.CASCADE, max_length=300, default=2)
    

    def __str__(self):
        return self.skill

class Certificate(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images', default='')

    def __str__(self):
        return self.title


