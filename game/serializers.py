from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
	"""Serializer to map the Model instance into JSON format."""
	class Meta:
		"""Meta class to map serializer's fields with the model fields."""
		model = User
		fields = '__all__'
		read_only_fields = ()
		extra_kwargs = {'url': {'view_name': 'users:user-detail', }}

	def create(self, validated_data):
		return(User.objects.create(**validated_data))

	def update(self, instance, validated_data):
		for field in validated_data:
			if field == 'password':
				instance.set_password(validated_data.get(field))
			else:
				instance.__setattr__(field, validated_data.get(field))
		instance.save()
		return(instance)

# # Serialize Python object to JSON string. 
# task_data = TaskSerializer(task).data 
 
# # Create Python object from JSON string.
# task_data = TaskSerializer(request.data)
# task = task_data.create() 

class GameSessionSerializer(serializers.ModelSerializer):
	class Meta:
		model = GameSession
		fields = '__all__'
		read_only_fields=('date_created')

class GameSessionBasicSerializer(serializers.ModelSerializer):
	class Meta:
		model = GameSessionBasic
		fields = '__all__'

class GameSessionMemberSerializer(serializers.ModelSerializer):
	class Meta:
		model = GameSessionBMember
		fields = '__all__'

class GameSessionSubmissionSerializer(serializers.ModelSerializer):
	class Meta:
		model = GameSessionSubmission
		fields = '__all__'

class GameBuyerDataSerializer(serializers.ModelSerializer):
	class Meta:
		model = GameBuyerData
		fields = '__all__'

class GameSupplierSettingsSerializer(serializers.ModelSerializer):
	class Meta:
		model = GameSupplierSettings
		fields = '__all__'

class GameSupplierDataSerializer(serializers.ModelSerializer):
	class Meta:
		model = GameSupplierData
		fields = '__all__'

class GameSettingsSerializer(serializers.ModelSerializer):
	class Meta:
		model = GameSettings
		fields = '__all__'

class VisibilityGameSettingsSerializer(serializers.ModelSerializer):
	class Meta:
		model = VisibilityGameSettings
		fields = '__all__'

class GameParameterSerializer(serializers.ModelSerializer):
	class Meta:
		model = GameParameter
		fields = '__all__'

class CommentLogSerializer(serializers.ModelSerializer):
	class Meta:
		model = CommentLog
		fields = '__all__'


serializer = CommentSerializer(comment)
serializer.data
# {'email': 'leila@example.com', 'content': 'foo bar', 'created': '2016-01-27T15:17:10.375877'}
# At this point we've translated the model instance into Python native datatypes. To finalise the serialization process we render the data into json.



json = JSONRenderer().render(serializer.data)
json
# b'{"email":"leila@example.com","content":"foo bar","created":"2016-01-27T15:17:10.375877"}'

# deserialize

stream = BytesIO(json)
data = JSONParser().parse(stream)
serializer = CommentSerializer(data=data)
serializer.validated_data
# {'content': 'foo bar', 'email': 'leila@example.com', 'created': datetime.datetime(2012, 08, 22, 16, 20, 09, 822243)}

# If we want to be able to return complete object instances based on the validated data we need to implement one or both of the .create() and .update() methods. For example:

class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()

    def create(self, validated_data):
        return Comment(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.content = validated_data.get('content', instance.content)
        instance.created = validated_data.get('created', instance.created)
        return instance

# If your object instances correspond to Django models you'll also want to ensure that these methods save the object to the database. For example, if Comment was a Django model, the methods might look like this:

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.content = validated_data.get('content', instance.content)
        instance.created = validated_data.get('created', instance.created)
        instance.save()
        return instance

# Now when deserializing data, we can call .save() to return an object instance, based on the validated data.

comment = serializer.save()

# Calling .save() will either create a new instance, or update an existing instance, depending on if an existing instance was passed when instantiating the serializer class:

# .save() will create a new instance.
serializer = CommentSerializer(data=data)

# .save() will update the existing `comment` instance.
serializer = CommentSerializer(comment, data=data)

# Passing additional attributes to .save()
# Sometimes you'll want your view code to be able to inject additional data at the point of saving the instance. This additional data might include information like the current user, the current time, or anything else that is not part of the request data.

# You can do so by including additional keyword arguments when calling .save(). For example:

serializer.save(owner=request.user)
