from rest_framework import serializers
from rest_framework.viewsets import ReadOnlyModelViewSet

from distributor.models import Hospital, HospitalPhoneNumber, Donation, DonationDetail, NeedType, Measure, Region, \
    District, Locality, Statistic


class HospitalPhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = HospitalPhoneNumber
        fields = ['value']


class StatisticPhoneNumberSerializer(serializers.ModelSerializer):
    need_help = serializers.SerializerMethodField()

    class Meta:
        model = Statistic
        fields = ['name', 'actual', 'capacity', 'has_capacity', 'need_help']

    @staticmethod
    def get_need_help(obj):
        return True if obj.has_capacity and obj.actual > obj.capacity else False


class HospitalSerializer(serializers.HyperlinkedModelSerializer):
    phone_numbers = HospitalPhoneNumberSerializer(many=True, read_only=True)
    statistics = StatisticPhoneNumberSerializer(many=True, read_only=True)
    location = serializers.SerializerMethodField()

    class Meta:
        model = Hospital
        fields = ['id', 'name', 'code', 'address', 'location', 'phone_numbers', 'statistics']

    @staticmethod
    def get_location(obj):
        return {"longitude": obj.location.y, 'latitude': obj.location.x}


class MeasureTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measure
        fields = ['id', 'name']


class NeedTypeSerializer(serializers.ModelSerializer):
    measure = MeasureTypeSerializer()

    class Meta:
        model = NeedType
        fields = ['id', 'name', 'measure', 'price_per_piece']


class DonationDetailSerializer(serializers.ModelSerializer):
    need_type = NeedTypeSerializer(read_only=True)

    class Meta:
        model = DonationDetail
        fields = ['id', 'amount', 'need_type']


class DonationSerializer(serializers.HyperlinkedModelSerializer):
    details = DonationDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Donation
        fields = ['id', 'donator_name', 'donator_type', 'description', 'created_at', 'details']


class RegionSerializer(serializers.HyperlinkedModelSerializer, ReadOnlyModelViewSet):
    class Meta:
        model = Region
        fields = ['id', 'name']


class DistrictSerializer(serializers.HyperlinkedModelSerializer, ReadOnlyModelViewSet):
    class Meta:
        model = District
        fields = ['id', 'region_id', 'name']


class LocalitySerializer(serializers.HyperlinkedModelSerializer, ReadOnlyModelViewSet):
    class Meta:
        model = Locality
        fields = ['id', 'district_id', 'name']
