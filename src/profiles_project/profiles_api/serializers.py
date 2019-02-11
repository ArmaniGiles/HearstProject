from rest_framework import serializers
from  . import models


class UserProfileInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = ('id', 'name')


class CourseSerializer(serializers.ModelSerializer):
    users = serializers.SerializerMethodField()
    class Meta:
        model = models.Course
        fields = ('id', 'name', 'startDate', 'users')
        #  Course.objects.all()[0].courses.all()[0].name
    
    def get_users(self, obj):
        users = obj.courses.all()
        users = UserProfileInfoSerializers(users, many=True).data
        return users
        # return 'Ajay'

class HelloSerializer(serializers.Serializer):
    """ Serializers a name field for testing our APIView."""

    name = serializers.CharField(max_length=10) # it serializers the data
    #what does this acrually do?

    # def validate_name(self):
    #     #if len(self.name) <=2:
    #     pass
# MIddelWare->UrlDispatcher ->Views 

    #1 OPtion.) Views could render data to a website using Tempaltes
    #2 Option.) From Views you can send data into JSON format and this data is globaly accepted datatype for the RESTAPIs
    #Option 2 HAS to go to the Serializertions part
    #to convert queryset objects to JSON
    #2 ways to do Serializations
        # one way defualt there is a serializers method
class UserProfileSerializers(serializers.ModelSerializer):
    """A serializers for user profile objects."""
    print("At the top of UserProfileSerializers")
    courses = CourseSerializer(many=True)
    class Meta:
        model  = models.UserProfile
        fields = ('id','email','name','password', 'courses')
        extra_kwargs = {'password':{'write_only': True}}

    # def validate(self):
    #     if self.email in []:
    #         raise ValueError('email already exists.')
    #     pass

    def create(self,validated_data):
        """Create and return a new user."""
        
        print("(inside create) validated_data : ",validated_data)
        user = models.UserProfile(
            email=validated_data['email'],
            name=validated_data['name'],
        )
        print("user.is_active : ",user.is_active)
        user.set_password(validated_data['password'])
        user.save()
        print("user : ",user)

        

        return user