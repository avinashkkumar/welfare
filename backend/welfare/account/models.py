from django.db import models

# Create your models here.


from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os
import pathlib, uuid


class MyAccountManager(BaseUserManager):
	def create_user(self, email, firstName, lastName, password=None):
		if not email:
			raise ValueError('Users must have an email address')
		if not username:
			raise ValueError('Users must have a username')

		user = self.model(
			email=self.normalize_email(email),
			username=firstName + lastName,
			firstName = firstName,
			lastName = lastName,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self,firstName, lastName, username, email, password=None):
		user = self.model(
			email=self.normalize_email(email),
			username=username,
			firstName = firstName,
			lastName = lastName,
		)
		user.set_password(password)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.is_student_member = False
		user.save(using=self._db)
		return user


class Account(AbstractBaseUser):
	firstName				= models.CharField( max_length = 30 ,null = True, blank =True)
	lastName				= models.CharField( max_length = 30 ,null = True, blank =True)
	username 				= models.CharField(max_length=30,unique=True)
	email 					= models.EmailField(verbose_name="email", max_length=60, unique=True)
	is_admin				= models.BooleanField(default=False)
	is_active				= models.BooleanField(default=True)
	is_staff				= models.BooleanField(default=False)
	is_superuser			= models.BooleanField(default=False)
	is_seller       		= models.BooleanField(default=True)
	date_joined				= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)
	

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['firstName','lastName','email']

	objects = MyAccountManager()

	def __str__(self):
		return self.username
	
	# For checking permissions. to keep it simple all admin have ALL permissons
	def has_perm(self, perm, obj=None):
		return self.is_admin

	def has_module_perms(self,app_label):
		return True




# use this upload handler for any file upload.
def uploadHandler(instance,filename):
    fpath = pathlib.Path(filename)
    newFileName = str(uuid.uuid1())
    return f"images/profile/{newFileName}{fpath.suffix}"