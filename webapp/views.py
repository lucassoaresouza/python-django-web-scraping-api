from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from bs4 import BeautifulSoup
import request

# Create your views here.
class ProductList(generics.ListCreateAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class WebScraping:

    htmlUrl = 'https://nerdstore.com.br/categoria/especiais/game-of-thrones/'
    htmlPage = ''
    productList = []

    def __init__():
        getHTMLPage()

    def setHTMLPage():
        req = request.get(this.htmlUrl)
        if(req.status_code == 200):
            this.htmlPage = BeautifulSoup(req.contend,'html.parser')
        else:
            this.htmlPage = None