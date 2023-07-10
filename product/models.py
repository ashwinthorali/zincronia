from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from roopale.getusername import get_request

# Create your models here.
class TopMenu(models.Model):
    description = models.CharField(max_length = 900)
    slug = models.CharField(max_length = 156, blank=True, null=True)
    keyword = models.CharField(max_length = 156)
    title = models.CharField(max_length = 156)
    og_type =models.CharField(max_length = 156)
    og_card = models.CharField(max_length = 156)
    og_site = models.CharField(max_length = 156)
    image  = models.ImageField(upload_to="SEO")
    canonical = models.CharField(max_length = 900, default="https://website.com/")
    order  = models.IntegerField(blank=True, null=True)
    
    menu_name  = models.CharField(max_length = 156)
    
    def submenu(self):
        data = SubMenu.objects.filter(menu_name=self.id).count()
        if data:
            return SubMenu.objects.filter(menu_name=self.id).order_by('order')
        else:
            return None    

    def direct_menu(self):
        data = Products.objects.filter(menu_name=self.id).count()
        if data:
            return Products.objects.filter(menu_name=self.id).order_by('order')
        else:
            return None  

    def __str__(self):
        return self.menu_name



# Create your models here.
class SubMenu(models.Model):
    description = models.CharField(max_length = 900)
    slug = models.CharField(max_length = 156, blank=True, null=True)
    keyword = models.CharField(max_length = 156)
    title = models.CharField(max_length = 156)
    og_type =models.CharField(max_length = 156)
    og_card = models.CharField(max_length = 156)
    og_site = models.CharField(max_length = 156)
    image  = models.ImageField(upload_to="SEO")
    canonical = models.CharField(max_length = 900, default="https://website.com/")
    menu_name  = models.ForeignKey(TopMenu, on_delete=models.CASCADE)
    sub_menu_name  = models.CharField(max_length = 156)
    order  = models.IntegerField(blank=True, null=True)
    

    def __str__(self):
        return self.sub_menu_name        


class Color(models.Model):
    color = models.CharField(max_length = 900)
    def __str__(self):
        return self.color        

class Size(models.Model):
    size = models.CharField(max_length = 900)
    def __str__(self):
        return self.size        

class Category(models.Model):
    category = models.CharField(max_length = 900)
    def __str__(self):
        return self.category        

class Tag(models.Model):
    tag = models.CharField(max_length = 900)
    def __str__(self):
        return self.tag        

class Shade(models.Model):
    shade = models.CharField(max_length=230)
    def __str__(self):
        return self.shade
    
class Specification(models.Model):
    specification = models.CharField(max_length=230)
    def __str__(self):
        return self.specification



# Create your models here.
class Products(models.Model):
    meta_description = models.CharField(max_length = 900)
    slug = models.CharField(max_length = 156,blank=True, null=True)
    keyword = models.CharField(max_length = 156)
    title = models.CharField(max_length = 156)
    og_type =models.CharField(max_length = 156)
    og_card = models.CharField(max_length = 156)
    og_site = models.CharField(max_length = 156)
    image  = models.ImageField(upload_to="SEO")
    canonical = models.CharField(max_length = 900, default="https://website.com/")
    order  = models.IntegerField(blank=True, null=True)
    menu_name  = models.ForeignKey(TopMenu, related_name='top_menu_name', on_delete=models.CASCADE, blank=True, null=True)
    sub_menu_name  = models.ForeignKey(SubMenu, on_delete=models.CASCADE, blank=True, null=True)
    sold_out = models.BooleanField(default=False)
    product_name  = models.CharField(max_length = 156,blank=True, null=True)
    note = models.CharField(max_length = 156,blank=True, null=True)
    short_desc = models.TextField(max_length = 1156,blank=True, null=True)   
    category  = models.ManyToManyField(Category,blank=True, null=True)
    tag  = models.ManyToManyField(Tag,blank=True, null=True)
    review =  models.IntegerField(blank=True, null=True)
    discount =  models.IntegerField(blank=True, null=True)
    range_of = models.CharField(max_length = 156,blank=True, null=True)
    sp = models.IntegerField(blank=True, null=True)
    color_shade = models.ManyToManyField(Shade, related_name='p_shade', blank=True, null=True)
    size_specification = models.ManyToManyField(Specification, related_name='s_spec', blank=True, null=True)
    
    featured  = models.BooleanField(default=False)
    trending  = models.BooleanField(default=False)
    new_arrival  = models.BooleanField(default=False)
    best_seller  = models.BooleanField(default=False)
    
    description = RichTextUploadingField(blank=True, null=True)
    addional_info = RichTextUploadingField(blank=True, null=True)
    created_on  = models.DateField(auto_now_add=True)
    updated_on  = models.DateField(auto_now=True)
    

    img1 = models.ImageField(upload_to="Product", blank=True, null=True)
    img1_alt = models.CharField(max_length = 156,blank=True, null=True)
    
    img2 = models.ImageField(upload_to="Product", blank=True, null=True)
    img2_alt = models.CharField(max_length = 156,blank=True, null=True)
    
    img3 = models.ImageField(upload_to="Product", blank=True, null=True)
    img3_alt = models.CharField(max_length = 156,blank=True, null=True)
    
    img4 = models.ImageField(upload_to="Product", blank=True, null=True)
    img4_alt = models.CharField(max_length = 156,blank=True, null=True)
    
    img5 = models.ImageField(upload_to="Product", blank=True, null=True)
    img5_alt = models.CharField(max_length = 156,blank=True, null=True)
    
    img6 = models.ImageField(upload_to="Product", blank=True, null=True)
    img6_alt = models.CharField(max_length = 156,blank=True, null=True)
    
    def mappedprice(self):
        item = MapPriceList.objects.filter(product=self.id)
        return item


    def cartitem(self):
        try:
            a = get_request().user    
            item = Cart.objects.filter(user=a, product=self.id).count()
            if item > 0:
                return True
            else:
                return False
        except:
            pass
    def thiscartitem(self):
        try:
            a = get_request().user    
            item = Cart.objects.filter(user=a, product=self.id).count()
            if item > 0:
                return Cart.objects.get(user=a, product=self.id)
            else:
                return None
        except:
            pass


    def inwishlist(self):
        try:
            a = get_request().user    
            item = Wishlist.objects.filter(user=a, product=self.id).count()
            if item > 0:
                return True
            else:
                return False        
        except:
            pass

    def cartitemCount(self):
        try:
            a = get_request().user   
            i = 0 
            item = Cart.objects.filter(user=a, product=self.id).count()
            if item > 0:
                q = Cart.objects.get(user=a, product=self.id)
                i = q.qty
                return i
            else:
                return i
        except:
            pass

    def cartitemID(self):
        try:
            a = get_request().user    
            item = Cart.objects.filter(user=a, product=self.id).count()
            if item > 0:
                q = Cart.objects.get(user=a, product=self.id)
                return q.id
            else:
                return 'abc'        
        except:
            pass
 
    def review(self):
        return Reviews.objects.filter(product=self.id).order_by('-id')[:5]

    def countReview(self):
        return Reviews.objects.filter(product=self.id).count()

    def averageReview(self):
        review = Reviews.objects.filter(product=self.id)
        totalReview = Reviews.objects.filter(product=self.id).count()
        total = 0
        for ie in review:
            total = total + int(ie.stars) 
        averageReview = round(total/totalReview)
        return averageReview



    def __str__(self):
        return self.product_name

class Reviews(models.Model):
    product = models.ForeignKey(Products, related_name="review_product_name", on_delete=models.CASCADE)
    stars  = models.CharField(max_length = 150)
    comment = models.TextField()
    name  = models.TextField()
    email = models.TextField()
    time  = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return str(self.name)
 
class MapPriceList(models.Model):
    product = models.ForeignKey(Products, related_name="map_product_name", on_delete=models.CASCADE)
    shade  = models.ForeignKey(Shade, related_name="shades_name",  on_delete=models.CASCADE)
    specification  = models.ForeignKey(Specification, related_name="specification_name",  on_delete=models.CASCADE)
    mrp = models.CharField(max_length = 156,blank=True, null=True)
    
    def __str__(self):
        return str(self.product)
    
class Cart(models.Model):
    user = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE)
    product = models.ForeignKey(Products, related_name="products_name", on_delete=models.CASCADE)
    qty  = models.IntegerField(blank=True, null=True)
    spec = models.IntegerField(blank=True, null=True)
    shade = models.IntegerField(blank=True, null=True)
    date  = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField(blank=True, null=True)


class CouponCode(models.Model):
    code = models.CharField(max_length=30)
    discount  = models.IntegerField(blank=True, null=True)
    times  = models.IntegerField(blank=True, null=True)
    max_sp_discount  = models.IntegerField(blank=True, null=True)
    one_user  = models.BooleanField()
    user = models.ForeignKey(User, related_name="CouponCodeuser", on_delete=models.CASCADE,blank=True, null=True)
    date  = models.DateTimeField(auto_now_add=True)


class CouponCodeUsage(models.Model):
    user = models.ForeignKey(User, related_name="CouponCode_user", on_delete=models.CASCADE,blank=True, null=True)
    coupon  = models.ForeignKey(CouponCode, on_delete=models.CASCADE, null=True)
    
    used = models.BooleanField(default=False)
    date  = models.DateTimeField(auto_now_add=True)
    


class Wishlist(models.Model):
    user = models.ForeignKey(User, related_name="user_wishlist", on_delete=models.CASCADE)
    product = models.ForeignKey(Products, related_name="product_wishlist", on_delete=models.CASCADE)
    qty  = models.IntegerField(blank=True, null=True)
    date  = models.DateTimeField(auto_now_add=True)


class Gallery(models.Model):
    name  = models.CharField(max_length = 150)
    image  = models.ImageField(upload_to="Gallery")
    date  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)



class Order(models.Model):
    user_id  = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number= models.CharField(max_length=101)
    first_name = models.CharField(max_length=310)
    last_name = models.CharField(max_length=310)
    company_name = models.CharField(max_length=310,blank=True, null=True)
    # email = models.EmailField(max_length=30)
    address = models.CharField(max_length=300)
    appartment_no  = models.CharField(max_length=130)
    city = models.CharField(max_length=130)
    country = models.CharField(max_length=1100, default='INDIA')
    zip_code = models.CharField(max_length=130)
    coupon_code = models.CharField(max_length=1200, blank=True, null=True)
    discount =  models.CharField(max_length=200, blank=True, null=True)
    total_amount  = models.IntegerField( blank=True, null=True)
    bill = models.TextField(max_length=11130, null=True, blank=True)
    payment_method = models.CharField(max_length=11200, blank=True, null=True)
    paid = models.BooleanField(default=False)
    payment_id = models.CharField(max_length=11200, blank=True, null=True)
    privacy_policy = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
    
    order_fulfilled = models.BooleanField(default=False)
    
    def __str__(self):
        return self.first_name

class NewsLetter(models.Model):
    email = models.CharField(max_length = 156,blank=True, null=True)
    date  = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.email)
 