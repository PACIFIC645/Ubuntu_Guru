# ubuntu_guru/models.py

from django.db import models

class Article(models.Model):
    """
    Represents a written article.

    Attributes:
        title (str): The title of the article.
        content (str): The body content of the article.
        published_date (datetime): The date and time the article was published.
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Returns a string representation of the article, which is its title.
        """
        return self.title
        