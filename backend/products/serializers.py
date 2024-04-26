from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Product
from . import validators

# You can have multiple serializers based on use case. Just assign different names.


class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk'
    )
    title = serializers.CharField(
        validators=[validators.validate_title_no_hello, validators.unique_product_title])
    # name = serializers.CharField(source='title', read_only=True) makes exact copy of with diff keywords
    # email = serializers.CharField(source='user.email', read_only=True)

    class Meta:
        model = Product
        fields = [
            # 'user',
            'url',
            'edit_url',
            'pk',
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount'
        ]

    # def create(self, validated_data):
    #     # return Product.obejcts.create(**validated_data)
    #     email = validated_data.pop('email')
    #     obj = super().create(validated_data)
    #     print(email, obj)
    #     return obj

    # def update(self, instance, validated_data):
    #     email = validated_data.pop('email')
    #     return super().update(instance, validated_data)

    def get_edit_url(self, obj):
        request = self.context.get('request')  # self.request
        if request is None:
            return None
        return reverse("product-edit", kwargs={"pk": obj.pk}, request=request)

    def get_my_discount(self, obj):
        print(obj.id)
        return obj.get_discount()
        # Obj is the instance of the serializer and from it many data can be derived
        # if we had a user in the instance, we can: obj.user -> user.username
        # if we had a user in the instance, we can: obj.catergory -> user.category
