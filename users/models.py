from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.db.models import Q


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, role='EMPLOYEE', **extra_fields):
        if not email:
            raise ValueError(_("The Email field must be set"))
        if not username:
            raise ValueError(_("The Username field must be set"))
        
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, role=role, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('role', 'ADMIN')
        extra_fields.setdefault("is_lead", True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_lead") is not True:
            raise ValueError("Superuser must have is_lead=True.")
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(username, email, password, **extra_fields)

    def get_by_natural_key(self, identifier):
        return self.get(Q(username=identifier) | Q(email=identifier))


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    role_choices = [
        ("ADMIN", "ADMIN"),
        ("EMPLOYEE", "EMPLOYEE"),
    ]
    designation_choices = [
        ("Developer Trainee", "Developer Trainee"),
        ("Developer", "Developer"),
        ("Senior Developer", "Senior Developer"),
        ("Intern-Software Development", "Intern-Software Development"),
        ("Intern-Machine Learning", "Intern-Machine Learning"),
        ("Junior Developer", "Junior Developer"),
        ("Project Coordinator", "Project Coordinator"),
        ("Product Manager", "Product Manager"),
        ("Machine Learning Engineer", "Machine Learning Engineer"),
        ("DevOps Engineer", "DevOps Engineer"),
        ("UI/UX Designer", "UI/UX Designer"),
        ("Quality Assurance Engineer", "Quality Assurance Engineer"),
        ("Lead Frontend Engineer", "Lead Frontend Engineer"),
        ("Lead Backend Engineer", "Lead Backend Engineer"),
        ("HR Manager", "HR Manager"),
        ("IT Specialist", "IT Specialist"),
        ("Business Analyst", "Business Analyst"),
        ("Sales Manager", "Sales Manager"),
        ("Marketing Executive", "Marketing Executive"),
        ("CTO", "CTO"),
        ("CEO", "CEO"),
    ]
    role = models.CharField(max_length=10, choices=role_choices, default="EMPLOYEE")
    designation = models.CharField(max_length=30, choices=designation_choices, default="Developer Trainee")
    is_lead = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    employee_id = models.IntegerField(null=True, blank=True, unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10)
    contact_no = models.IntegerField(null=True, blank=True, unique=True)
    date_of_joining = models.DateField(null=True, blank=True)
    office_location = models.CharField(max_length=25)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'  # Primary unique identifier for the user
    REQUIRED_FIELDS = ['email']  # Fields required when creating superuser

    def __str__(self):
        return self.username
