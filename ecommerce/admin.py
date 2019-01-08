from django.contrib import admin

from ecommerce.models import Category, Product, ProductHasImage, ProductReview, WishList, Cart


class ProductHasImageInline(admin.TabularInline):
    model = ProductHasImage


class AdminProduct(admin.ModelAdmin):
    inlines = [ProductHasImageInline]


admin.site.register(Category)

admin.site.register(Product, AdminProduct)

admin.site.register(ProductReview)

# admin.site.register(ProductHasImage)

admin.site.register(WishList)

admin.site.register(Cart)
