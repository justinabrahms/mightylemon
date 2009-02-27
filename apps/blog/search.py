import solango
from blog.models import Post


class PostDocument(solango.SearchDocument):
    title = solango.fields.CharField(copy=True)
    date = solango.fields.DateField()
    body = solango.fields.TextField(copy=True)

    def transform_date(self, instance):
        return instance.pub_date

solango.register(Post, PostDocument)
