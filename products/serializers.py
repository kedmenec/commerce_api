from rest_framework import serializers
from products.models import Product, Review
from django.contrib.auth.models import User, Group
from rest_framework.exceptions import APIException

class Conflict(APIException):
    '''Custom exception to return 409 conflict if user is trying to add
    multiple reviews for the same product.
    '''
    status_code = 409
    default_detail = 'User has already reviewed this product.'
    default_code = 'conflict'


class ProductSerializer(serializers.ModelSerializer):

    reviews = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'title', 'price', 'colour', 'category', 'image', 'reviews')

class ReviewSerializer(serializers.ModelSerializer):
    # Set the user to the logged in user on create.
    user = serializers.PrimaryKeyRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Review
        fields = ('id', 'text', 'user', 'rating', 'product')

    def create(self, validated_data):
        # If the user has already reviewed the product, return an error
        for review in validated_data['product'].reviews.all():
            if review.user == validated_data['user']:
                raise Conflict()
        else:
            # return the created review object.
            r = Review(**validated_data)
            r.save()
            return r


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')