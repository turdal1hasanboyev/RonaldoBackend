from django.db import models

#abstractuser
from django.contrib.auth.models import AbstractUser
#ckeditor
from ckeditor.fields import RichTextField
# slug
from django.template.defaultfilters import slugify
#get absolute url
from django.urls import reverse


class BaseModel(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class User(BaseModel, AbstractUser):
    bio = RichTextField(null=True, blank=True)
    date_birth = models.CharField(max_length=225, null=True, blank=True)
    address = models.CharField(max_length=225, null=True, blank=True)
    zip_code = models.IntegerField(default=0, null=True, blank=True)
    phone_number = models.CharField(max_length=225, null=True, blank=True)
    avatar = models.ImageField(upload_to='Avatar/', null=True, blank=True)
    complated_project = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.username
    

class Company(BaseModel):
    name = models.CharField(max_length=225, null=True, blank=True)
    image = models.ImageField(upload_to='CompanyIimage/', null=True, blank=True)

    def __str__(self):
        return self.name
    

class Education(BaseModel):
    name = models.CharField(max_length=225, null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    direction = models.CharField(max_length=225, null=True, blank=True)
    date = models.CharField(max_length=225, null=True, blank=True)

    def __str__(self):
        return self.name
    

class Experience(BaseModel):
    name = models.CharField(max_length=225, null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    education = models.CharField(max_length=225, null=True, blank=True)
    date = models.CharField(max_length=225, null=True, blank=True)

    def __str__(self):
        return self.name


class Awards(BaseModel):
    name = models.CharField(max_length=225, null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    date = models.CharField(max_length=225, null=True, blank=True)
    image = models.ImageField(upload_to='AwardImage/', null=True, blank=True)
    education = models.CharField(max_length=225, null=True, blank=True)

    def __str__(self):
        return self.name
    

class Skills(BaseModel):
    name = models.CharField(max_length=225, null=True, blank=True)
    percentage = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.name
    

class Services(BaseModel):
    name = models.CharField(max_length=225, null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='ServiceImage/', null=True, blank=True)

    def __str__(self):
        return self.name
    

class OurProjects(BaseModel):
    name = models.CharField(max_length=225, null=True, blank=True)
    image = models.ImageField(upload_to='ProjectImage/', null=True, blank=True)
    service = models.ForeignKey(Services, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
    

class SiteAdminisration(BaseModel):
    awards = models.IntegerField(default=0, null=True, blank=True)
    projects = models.IntegerField(default=0, null=True, blank=True)
    happy_customers = models.IntegerField(default=0, null=True, blank=True)
    cups_of_cofee = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return f"{self.awards}"
    

class GetInTouch(BaseModel):
    name = models.CharField(max_length=225, null=True, blank=True)
    email = models.EmailField(max_length=225, null=True, blank=True, unique=True)
    message = RichTextField(null=True, blank=True)
    subject = models.CharField(max_length=225, null=True, blank=True)

    def __str__(self):
        return self.name
    

class Category(BaseModel):
    slug = models.SlugField(unique=True, max_length=225, null=True, blank=True)
    name = models.CharField(max_length=225, null=True, blank=True)

    def save(self, *args, **kwargs):  
        if not self.slug:
            self.slug = slugify(self.name)

        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    

class Tag(BaseModel):
    slug = models.SlugField(unique=True, max_length=225, null=True, blank=True)
    name = models.CharField(max_length=225, null=True, blank=True)

    def save(self, *args, **kwargs):  
        if not self.slug:
            self.slug = slugify(self.name)

        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    

class Blog(BaseModel):
    name = models.CharField(max_length=225, null=True, blank=True)
    slug = models.SlugField(unique=True, max_length=225, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    image = models.ImageField(upload_to='Blogs/', null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    description_2 = RichTextField(null=True, blank=True)
    content_name = models.CharField(max_length=225, null=True, blank=True)
    content = RichTextField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def get_absolute_url(self):
        return reverse("single", kwargs={"slug": self.slug})
    
    def save(self, *args, **kwargs):  
        if not self.slug:
            self.slug = slugify(self.name)

        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    

class Comment(BaseModel):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=225, null=True, blank=True)
    email = models.EmailField(max_length=225, null=True, blank=True)
    message = RichTextField(null=True, blank=True)
    web_site = models.URLField(null=True, blank=True, unique=True)

    def __str__(self):
        return self.name
    