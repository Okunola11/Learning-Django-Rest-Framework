from rest_framework import serializers

from .models import Product

# You can have multiple serializers based on use case. Just assign different names.

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = ['title', 'content', 'price', 'sale_price', 'my_discount']

    def get_my_discount(self, obj):
        print(obj.id)
        return obj.get_discount()
        # Obj is the instance of the serializer and from it many data can be derived
        # if we had a user in the instance, we can: obj.user -> user.username
        # if we had a user in the instance, we can: obj.catergory -> user.category
