from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from bs4 import BeautifulSoup
import requests

# Create your views here.
class WebScrapingView:

    htmlUrl = 'https://nerdstore.com.br/categoria/especiais/game-of-thrones/'
    htmlPage = ''
    htmlLiProductsTag = []
    productList = []

    def __init__(self):
        self.setHTMLPage()
        self.setLiProductsTag()
        self.getProductData()
        self.saveProductData()

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

    def getProductName(self,index):
        name = self.htmlLiProductsTag[index].find("h2",{"class":"woocommerce-loop-product__title"})
        name = name.next
        return name

    def getProductPrice(self,index):
        price = self.htmlLiProductsTag[index].find_all("span",{"class":"woocommerce-Price-amount"})
        price = price[1].next.next.next
        price = price.replace(',','.')
        price = float(price)
        return price

    def getProductImage(self,index):
        image = self.htmlLiProductsTag[index].find("img")
        image = image["src"]
        return image

    def getProductData(self):
        for index in range(len(self.htmlLiProductsTag)):
            if(self.htmlLiProductsTag != None):
                name = self.getProductName(index=index)
                price = self.getProductPrice(index=index)
                image = self.getProductImage(index=index)
                self.productList.append({
                                        "name":name,
                                        "price":price,
                                        "image":image
                                        })
            else:
                return none

    def saveProductData(self):
        for product in self.productList:
            if(product != None):
                Product.objects.update_or_create(
                                                name=product["name"],
                                                price=product["price"],
                                                images=[product["image"]]
                                                )


class ProductList(generics.ListCreateAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    scraping = WebScrapingView()