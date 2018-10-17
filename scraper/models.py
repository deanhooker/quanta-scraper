from django.db import models

class Article(models.Model):
    """An article's headline information."""
    title = models.CharField(max_length=200, primary_key=True)
    excerpt = models.TextField()
    link = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns the article title."""
        return self.title