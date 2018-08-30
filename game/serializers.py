from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
	"""Serializer to map the Model instance into JSON format."""
	class Meta:
		model = User
		fields = '__all__'
		# read_only_fields = ()
		# extra_kwargs = {'url': {'view_name': 'users:user-detail',}}

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


class GameSessionSerializer(serializers.ModelSerializer):
	class Meta:
		model = GameSession
		fields = '__all__'
		read_only_fields = ('date_created')


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

	def create(self, validated_data):
		return(Comment.objects.create(**validated_data))

	def update(self, instance, validated_data):
		instance.email = validated_data.get('email', instance.email)
		instance.content = validated_data.get('content', instance.content)
		instance.created = validated_data.get('created', instance.created)
		instance.save()
		return(instance)

		

# serializer = CommentSerializer(comment)
# json = JSONRenderer().render(serializer.data) 

# # deserialize
# data = JSONParser().parse(BytesIO(json))
# serializer = CommentSerializer(data=data)


# # .save() will create a new instance.
# serializer = CommentSerializer(data=data)

# # .save() will update the existing `comment` instance.
# serializer = CommentSerializer(comment, data=data)

