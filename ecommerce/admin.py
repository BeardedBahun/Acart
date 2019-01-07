from django.contrib import admin

from ecommerce.models import Category, Product, ProductHasImage, ProductReview, WishList, Cart

admin.site.register(Category)

admin.site.register(Product)

admin.site.register(ProductReview)

admin.site.register(ProductHasImage)

admin.site.register(WishList)

admin.site.register(Cart)
