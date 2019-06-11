Vojtechs-MBP:setup_project vojta$ docker-compose run setup_project sh -c "python setu
p_project/manage.py shell"
Python 3.7.2 (default, Dec 26 2018, 08:50:25)
[GCC 6.4.0] on linux

Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from news.models import Article
>>> from news.api.serializers import ArticleSerializer
>>> article_instance = Article.objects.first()
>>> article_instance
<Article: John Doe Happy Birthday ISS>
>>> serializer = ArticleSerializer(article_instance)
>>> serializer
ArticleSerializer(<Article: John Doe Happy Birthday ISS>):
    id = IntegerField(read_only=True)
    author = CharField()

    title = CharField()
    description = CharField()
    body = CharField()
    location = CharField()
    publication_date = DateField()
    active = BooleanField()
    created_at = DateTimeField(read_only=True)
    updated_at = DateTimeField(read_only=True)
>>> serializer.data
{'id': 1, 'author': 'John Doe', 'title': 'Happy Birthday ISS', 'description': 'Space
celebration', 'body': 'some content', 'location': 'England', 'publication_date': '201
9-06-10', 'active': True, 'created_at': '2019-06-10T18:58:53.728920Z', 'updated_at':
'2019-06-10T18:58:53.728975Z'}
>>> from rest_framework.renderers import JSONRenderer
>>> json = JSONRenderer().render(serializer.data)
>>> json
b'{"id":1,"author":"John Doe","title":"Happy Birthday ISS","description":"Space celeb
ration","body":"some content","location":"England","publication_date":"2019-06-10","a

ctive":true,"created_at":"2019-06-10T18:58:53.728920Z","updated_at":"2019-06-10T18:58
:53.728975Z"}'
>>> import io
>>> from rest_framework.parsers import JSONParser
>>> stream = io.BytesIO(json)
>>> data = JSONParser().parse(stream)
>>> data
{'id': 1, 'author': 'John Doe', 'title': 'Happy Birthday ISS', 'description': 'Space
celebration', 'body': 'some content', 'location': 'England', 'publication_date': '201
9-06-10', 'active': True, 'created_at': '2019-06-10T18:58:53.728920Z', 'updated_at':
'2019-06-10T18:58:53.728975Z'}
>>> serializer = ArticleSerializer(data=data)
>>> serializer.is_valid()
True
>>> serializer.validated_data
OrderedDict([('author', 'John Doe'), ('title', 'Happy Birthday ISS'), ('description',
 'Space celebration'), ('body', 'some content'), ('location', 'England'), ('publicati
on_date', datetime.date(2019, 6, 10)), ('active', True)])
>>> serializer.save()
{'author': 'John Doe', 'title': 'Happy Birthday ISS', 'description': 'Space celebrati
on', 'body': 'some content', 'location': 'England', 'publication_date': datetime.date
(2019, 6, 10), 'active': True}
<Article: John Doe Happy Birthday ISS>
>>> Article.objects.all()
<QuerySet [<Article: John Doe Happy Birthday ISS>, <Article: John Doe Happy Birthday
ISS>]>
