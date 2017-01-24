
# Create your tests here.
from b20.models import AliveQuestions

# Tb7GZw8DVkQ=
x = AliveQuestions.objects.get(qid=input())
print(x)
