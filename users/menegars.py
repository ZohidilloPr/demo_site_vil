from django.contrib.auth.models import BaseUserManager

class CustomUsersMenegar(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('Usernameni kiriting!')
        user = self.model(
            username=username,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_staffuser(self, username, password, **extra_fields):
        user = self.create_user(
            username,
            password=password,
            **extra_fields
        )
        user.staff = True
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, password):
        user = self.create_user(
            username,
            password
        )
        user.staff = True
        user.superuser = True
        user.data_viewer = True
        user.save(using=self._db)
        return user