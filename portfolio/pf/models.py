from django.db import models

# Create your models here.

#Model for Catagory, which will describe what a blog contains
#Fields needed: catagoryName
class Catagory(models.Model):
    catagoryName = models.TextField(max_length=75, help_text="Name for catagory")

    def __str__(self):
        #String for representing the catagory object.
        return f'{self.catagoryName}'

#Model for Blog, which will contain the posts I make
#Fields needed: BlogName, catagories
class Blog(models.Model):
    blogName = models.TextField(max_length=100, help_text="Name for the blog")
    catagories = models.ManyToManyField(Catagory,
        help_text="Catagories relevant to blog being created.")

    def __str__(self):
        #String for representing the blog object.
        return f'{self.blogName}'

#Model for Message, which will belong to a blog
#Fields needed: Blog, title, content, datePublished, image
class Message(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="messages")
    title = models.TextField(max_length=100, help_text="Title of the message")
    content = models.TextField(max_length=500, help_text="Content of the message")
    datePublished = models.DateTimeField()
    image = models.ImageField(upload_to="images", width_field='width', height_field='height')

    def __str__(self):
        #String for representing the message object.
        return f'{self.title}'
