from app1.models import School
from app1.models import Student
from rest_framework import serializers


class SchoolSerializers(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = [
            "id",
            "school_name",
            "teacher_strength",
            "class_strength",
            "contact_number",
        ]

        def create(self, validated_data):
            return School.objects.create(
                validated_data=[
                    "school_name",
                    "teacher_strength",
                    "class_strength",
                    "contact_number",
                ]
            )

        # school_name=serializers.CharField(max_length=60)

    # teacher_strength=serializers.CharField(max_length=20)
    # class_strength=serializers.CharField(max_length=20)
    # contact_number=serializers.CharField(max_length=20)


class StudentSerializers(serializers.ModelSerializer):
    School_name1 = SchoolSerializers()

    class Meta:
        model = Student
        fields = [
            "id",
            "enrollment_number",
            "first_name",
            "last_name",
            "class_name1",
            "School_name1",
        ]

    # School_name1 = serializers.SerializerMethodField()
    # def  get_product_id(self, obj):
    #     if obj.School_name1 is not None:
    #         return obj.School_name1.id
    #     return None

    # school=serializers.HyperlinkedRelatedField(many=True,read_only=True ,view_name='school-detail')
    # comments_rel=serializers.StringRelatedField(many=True,read_only=True)
    # school=serializers.PrimaryKeyRelatedField(many=True,read_only=True)

    # def create(self, validated_data):
    #     school_data = validated_data.pop('School_name1')
    #     school_instance, _ = School.objects.create(validated_data["school_name"],validated_data["teacher_strength"],validated_data["class_strength"],validated_data["contact_number"])

    #     student = Student.objects.create(School_name1=school_instance, **validated_data)
    #     return student

    # enrollment_number=serializers.CharField(max_length=30)
    # first_name=serializers.CharField(max_length=30)
    # last_name=serializers.CharField(max_length=20)
    # class_name1=serializers.CharField(max_length=20)
    # School_name1=serializers.ForeignKey(School)
