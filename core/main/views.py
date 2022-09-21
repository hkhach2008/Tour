from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Home, HomeProduct, HomeProduct1, HomeProduct2, Eror404, Checkout, Footer, Category, Shoose, Category2, Brand, ShopProduct, Product_detail, Blog, BlogSingle, BlogSingle2, Cart

# Create your views here.

class HomeListView(ListView):
    template_name = 'index.html'

    def get(self, request):
        homes = Home.objects.all()
        product = HomeProduct.objects.all()
        product1 = HomeProduct1.objects.all()
        product2 = HomeProduct2.objects.all()
        cats = Category.objects.all()
        cats2 = Category2.objects.all()
        cats3 = Brand.objects.all()
        return render(request, self.template_name, {'homes':homes, 
                                                    'product':product, 
                                                    'product1':product1,
                                                    'product2':product2,
                                                    'cats':cats,
                                                    'cats2':cats2,
                                                    'cats3':cats3
                                                    })

class ShopListView(ListView):
    template_name = 'shop.html'
    
    def get(self, request):
        shop = ShopProduct.objects.all()
        return render(request, self.template_name,{'shop':shop})





class ErorListView(ListView):
    template_name = '404.html'
    
    def get(self, request):
        eror = Eror404.objects.all()
        return render(request, self.template_name,{'eror':eror})




class CheckoutListView(ListView):
    template_name = 'checkout.html'
    
    def get(self, request):
        checkouts = Checkout.objects.all()
        return render(request, self.template_name,{'checkouts':checkouts})



class FooterListView(ListView):
    template_name = 'base.html'
    
    def get(self, request):
        footers = Footer.objects.all()
        return render(request, self.template_name,{'footers':footers})




class ProductListView(ListView):
    template_name = 'product_detail.html'
    
    def get(self, request):
        product = Product_detail.objects.all()
        return render(request, self.template_name,{'product':product})




class BlogListView(ListView):
    template_name = 'blog_list.html'
    
    def get(self, request):
        blogs = Blog.objects.all()
        return render(request, self.template_name,{'blogs':blogs})





class BlogSingleListView(ListView):
    template_name = 'blog_single.html'
    
    def get(self, request):
        blogsing = BlogSingle.objects.all()
        blogsing2 = BlogSingle2.objects.all()
        return render(request, self.template_name,{'blogsing':blogsing, 'blogsing2':blogsing2})





class CartListView(ListView):
    template_name = 'cart.html'
    
    def get(self, request):
        carts = Cart.objects.all()
        return render(request, self.template_name,{'carts':carts})






def contact(request):
    return render(request, 'contact.html')




def login(request):
    return render(request, 'login.html')












