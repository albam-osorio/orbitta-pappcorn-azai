from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Ocupacion(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = _('Ocupación')
        verbose_name_plural = _('Ocupaciones')

# https://www.fomfus.com/articles/how-to-use-email-as-username-for-django-authentication-removing-the-username
class UsuarioManager(UserManager):
    """Define un model manager para el modelo Usuario en el cual el atributo username no es requerido."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Crea y guarda un usuario con el correo electrónico y la contraseña especificados."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        username = email
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Crea y guarda un usuario regular con el correo electrónico y la contraseña especificados."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Crea y guarda un super usuario con el correo electrónico y la contraseña especificados."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Un super usuario debe tener is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Un super usuario debe tener is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class Usuario(AbstractUser):
    """
    Los usuarios de este proyecto son una especialización de la clase AbstractUser usada por el sistema de autenticación de Django.

    El password y el email son requeridos. El username = email
    """

    email = models.EmailField(_('email address'), unique=True) # changes email to unique and blank to false

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # removes email from REQUIRED_FIELDS

    # numero_identificacion = models.CharField(max_length=10, blank=False, null=False)
    # telefono = models.CharField(max_length=50, blank=False, null=False)
    # ocupacion = models.ForeignKey(Ocupacion, on_delete=models.PROTECT, null=True)



    # AbstractBaseUser
    # password
    # last_login
    # is_active

    # AbstractUser
    # username
    # first_name
    # last_name
    # email
    # is_staff
    # is_active
    # date_joined
    # EMAIL_FIELD
    # USERNAME_FIELD
    # REQUIRED_FIELDS

    # AbstractBaseUser
    # Stores the raw password if set_password() is called so that it can
    # be passed to password_changed() after the model is saved.
    # self.password = make_password(raw_password)
    # self._password = raw_password

    # AbstractUser
    # def clean(self):
    #     super().clean()
    #     self.email = self.__class__.objects.normalize_email(self.email)
    # def email_user(self, subject, message, from_email=None, **kwargs):
    #     """Send an email to this user."""
    #     send_mail(subject, message, from_email, [self.email], **kwargs)


