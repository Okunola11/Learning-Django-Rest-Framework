from rest_framework import generics, mixins, permissions, authentication
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from django.http import Http404
from django.shortcuts import get_object_or_404

from .models import Product
from .serializers import ProductSerializer
from .permissions import IsStaffEditorPermission


class ProductListCreateApiView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

    def perform_create(self, serializer):
        # print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        if content is None:
            content = title
        serializer.save(content=content)


class ProductDetailApiView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # has a look_up field = pk 'Primary Key'


product_detail_view = ProductDetailApiView.as_view()
# we can add this to our url or do as done for ProductListCreateApiView and add .as_view() to our urls file


class ProductUpdateApiView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title


product_update_view = ProductUpdateApiView.as_view()


class ProductDestroyApiView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # has a look_up field = pk

    def perform_destroy(self, instance):
        # instance - anything to run on the instance
        return super().perform_destroy(instance)


product_destroy_view = ProductDestroyApiView.as_view()


class ProductListApiView(generics.ListAPIView):
    '''
    we won't be using this method. We can do a ProductListCreateView as done above.
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

##################################################################################################
# Using Mixins and GenericAPIView (A single Class-based View)
# to define and understand how the generics used above were derived for the
# different CRUD operations.


class ProductMixinView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        print(args, kwargs)
        pk = kwargs.get('pk')  # if there is an arg for a single Product/Item
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        # print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        if content is None:
            content = title
        serializer.save(
            content='A single class based Mixins doing cool stuffs')


product_mixin_view = ProductMixinView.as_view()


###################################################################################################
# Using function based view this time around:
# This will be a single view to replace the ProductListCreate and ProductDetail views above
@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method

    if method == 'GET':
        if pk is not None:
            # detail view
            # returns the obj if it exists or err 404 if not
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data
            return Response(data)
        # list view
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data
        return Response(data)

    if method == 'POST':
        # Post/Create content
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content')
            if content is None:
                content = title

            serializer.save(content=content)
            return Response(serializer.data)
        return Response({'Invalied': 'not good data'}, status=400)
