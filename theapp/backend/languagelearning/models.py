from django.db import models

# Create your models here.


"""
    Text model: It holds the texts, their title, and number of words

    TODO:
        -Text compression
        -More fields related to words and stats
"""
class Text(models.Model):

    id = models.UUIDField(primary_key=True, editable=False)

    added = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True)

    content = models.TextField()
    words = models.ManyToManyField("Word", default='')
    class Meta:
        ordering =['added']

    def __str__(self):
        return self.title

"""
    Word model: it holds individual words, and they are related to
    a meaning.
"""
class Word(models.Model):

    added = models.DateTimeField(auto_now_add=True)
    wordStr = models.CharField(max_length=100)
    known = models.IntegerField()

    def __str__(self):
        return self.wordStr

"""
    Meaning model: describes a meaning of a concept, which is related to
    many words.
"""

class Meaning(models.Model):

    added = models.DateTimeField(auto_now_add=True)
    meaning = models.TextField()
    relatedWords = models.ForeignKey(Word, 
                                    on_delete=models.CASCADE, 
                                    default='')

