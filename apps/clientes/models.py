from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class ClienteManager(BaseUserManager):
    def create_user(self, correo, nombres, apellido_paterno, apellido_materno, password=None, **extra_fields):
        if not correo:
            raise ValueError('El usuario debe tener un correo electrónico')

        # Normalizamos el correo (pasarlo a minúsculas)
        correo = self.normalize_email(correo)
        extra_fields.setdefault('is_active', True)
        user = self.model(correo=correo, nombres=nombres, apellido_paterno=apellido_paterno, apellido_materno=apellido_materno, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, correo, nombres, apellido_paterno, apellido_materno, password=None, **extra_fields):
        extra_fields.setdefault('tipo_usuario', 'administrador')
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('El superusuario debe tener is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('El superusuario debe tener is_superuser=True.')

        return self.create_user(correo, nombres, apellido_paterno, apellido_materno, password, **extra_fields)

class Cliente(AbstractBaseUser, PermissionsMixin):
    TIPOS_USUARIO = (
        ('cliente', 'Cliente'),
        ('administrador', 'Administrador del Sistema'),
    )

    nombres = models.CharField(max_length=50, verbose_name="Nombres")
    apellido_paterno = models.CharField(max_length=50, verbose_name="Apellido Paterno")
    apellido_materno = models.CharField(max_length=50, verbose_name="Apellido Materno")
    correo = models.EmailField(max_length=128, unique=True, verbose_name="Correo")
    telefono = models.CharField(max_length=15, verbose_name="Teléfono")
    direccion = models.CharField(max_length=255, verbose_name="Dirección")
    tipo_usuario = models.CharField(max_length=15, choices=TIPOS_USUARIO, default='cliente', verbose_name="Tipo de Usuario")
    estado = models.BooleanField(default=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = ClienteManager()

    USERNAME_FIELD = 'correo'  # Campo de inicio de sesión será el correo electrónico
    REQUIRED_FIELDS = ['nombres', 'apellido_paterno', 'apellido_materno']

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        db_table = 'cliente'
        ordering = ['apellido_paterno', '-apellido_materno', 'nombres']

    def nombre_completo(self):
        return "{} {}, {}".format(self.apellido_paterno, self.apellido_materno, self.nombres)

    def __str__(self):
        return self.nombre_completo()
    
    @property
    def estado_display(self):
        return "Activo" if self.estado else "Inactivo"