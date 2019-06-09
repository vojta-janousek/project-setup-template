from django.http import JsonResponse

from products.models import Product, Manufacturer


def product_list(request):
    products = Product.objects.all()
    data = {'products': list(products.values())}
    response = JsonResponse(data)
    return response


def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        data = {'product': {
                    'name': product.name,
                    'manufacturer': product.manufacturer.name,
                    'description': product.description,
                    'photo': product.photo.url,
                    'price': product.price,
                    'shipping_cost': product.shipping_cost,
                    'quantity': product.quantity,
                }}
        response = JsonResponse(data)
    except Product.DoesNotExist:
        response = JsonResponse({
            'error': {
                'code': 404,
                'message': 'product not found'
            }},
            status=404)
    return response


def manufacturer_list(request):
    manufacturers = Manufacturer.objects.filter(active=True)
    data = {'manufacturers': list(manufacturers.values())}
    response = JsonResponse(data)
    return response


def manufacturer_detail(request, pk):
    try:
        manufacturer = Manufacturer.objects.get(pk=pk)

        # products = Product.objects.filter(manufacturer__name=manufacturer)
        # Alternative: use the model's related name (products)
        manufacturer_products = manufacturer.products.all()

        data = {'manufacturer': {
                    'pk': manufacturer.pk,
                    'name': manufacturer.name,
                    'location': manufacturer.location,
                    'active': manufacturer.active,
                    'products': list(manufacturer_products.values())
                }}
        response = JsonResponse(data)
    except Manufacturer.DoesNotExist:
        response = JsonResponse({
            'error': {
                'code': 404,
                'message': 'manufacturer not found'
            }},
            status=404)
    return response

# Basic Class Based Views
#
# from django.views.generic import DetailView, ListView
#
#
# class ProductDetailView(DetailView):
#     model = Product
#     template_name = 'products/product_detail.html'
#
#
# class ProductListView(ListView):
#     model = Product
#     template_name = 'products/product_list.html'
