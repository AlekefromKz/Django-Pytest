from django.db import models


class Privilege(models.Model):
    level = models.IntegerField()
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'Privilege: level={self.level}, name={self.name}'


class Role(models.Model):
    name = models.CharField(max_length=255)
    privileges = models.ManyToManyField(Privilege, related_name="roles")

    def __str__(self):
        return f'Role: name={self.name} privileges count={self.privileges.count()}'


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    birth_date = models.DateField()
    registered_on = models.DateTimeField(auto_now=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='people')

    class Meta:
        unique_together = ['first_name', 'last_name', 'birth_date']

    def __str__(self):
        return f'Person: {self.first_name} {self.last_name}'
