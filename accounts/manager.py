from django.contrib.auth.base_user import BaseUserManager



class userManager(BaseUserManager):

    def create_user(self, email, password = None, **extra_field):

        if not email:
            raise ValueError("Email is required")
        
        user = self.model(email = email, **extra_field)
        user.set_password(password)
        user.save(using = self._db)

        return user

    def create_superuser(self, email, password = None, **extra_field):

        extra_field.setdefault('is_staff', True)
        extra_field.setdefault('is_superuser', True)
        extra_field.setdefault('is_active', True)

        if extra_field.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_field.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        user = self.create_user(email, password, **extra_field)
        return user
