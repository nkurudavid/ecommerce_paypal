from django.contrib import admin
from django.utils.html import format_html

from .models import ProductCategory, Product, Order

# Register your models here.

class ProductInline(admin.TabularInline):
    model = Product
    extra = 0

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    search_fields = ('name',)
    inlines = (ProductInline,)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'quantity', 'image_display',)
    list_filter = ('category',)
    search_fields = ('name', 'description', 'category__name',)
    prepopulated_fields = {'image': ('name',)}
    fieldsets = (
        ('Product Info', {
            'fields': ('name', 'description', 'category',)
        }),
        ('Price', {
            'fields': ('price', 'quantity',)
        }),
        ('Image', {
            'fields': ('image',)
        }),
    )

    def image_display(self, obj):
        return format_html('<img src="{}" width="100" />'.format(obj.image.url))

    image_display.short_description = 'Image'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('orderCode', 'amount', 'is_paid', 'dateCreated',)
    list_filter = ('is_paid', 'dateCreated',)
    search_fields = ('orderCode',)
    readonly_fields = ('orderCode', 'amount', 'is_paid', 'dateCreated',)

    def has_add_permission(self, request):
        return False