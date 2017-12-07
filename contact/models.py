from django.db import models

class Message(models.Model):
    issue = models.CharField(max_length=200,blank=False)
    email = models.EmailField(blank=False)
    content = models.TextField(blank=False)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'mensaje del formulario de contacto'
        verbose_name_plural = 'mensajes del formulario de contacto'

    def __str__(self):
        return u'Mensaje de %s' % (self.email)
