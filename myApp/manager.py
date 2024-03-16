from django.contrib.auth.models import BaseUserManager

class customUserManager(BaseUserManager):
    def create_user(self, full_name, email, phone, password=None):
        if not full_name:
            raise ValueError("Enter Name")
        if not email:
            raise ValueError("Enter Email")
        if not phone:
            raise ValueError("Enter Phone")
        
        user = self.model(full_name=full_name, email=self.normalize_email(email), phone=phone)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, full_name, email, phone, password=None):
        user = self.create_user(full_name=full_name, email=email, phone=phone, password=password)
        user.is_active = True
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save(using=self._db)
        return user
