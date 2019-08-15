from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from bs4 import BeautifulSoup
import requests

# Create your views here.
class WebScrapingView:

    htmlUrl = 'https://nerdstore.com.br/categoria/especiais/game-of-thrones/'
    htmlPage = ''
    htmlLiProductsTag = ''
    productList = []

    def __init__(self):
        self.setHTMLPage()
        self.setLiProductsTag()

    def setHTMLPage(self):
        req = requests.get(self.htmlUrl)
        if(req.status_code == 200):
            self.htmlPage = BeautifulSoup(req.content,'html.parser')
        else:
            self.htmlPage = None

    def setLiProductsTag(self):
        liTag = []
        liTag = self.htmlPage.find_all("li",{"class":"product"})
        if(liTag != None):
            self.htmlLiProductsTag = liTag
        else:
            self.htmlLiProductsTag = None

class ProductList(generics.ListCreateAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    scraping = WebScrapingView()