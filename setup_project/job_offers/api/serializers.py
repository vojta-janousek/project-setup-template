from rest_framework import serializers

from job_offers.models import JobOffer


class JobOfferSerializer(serializers.ModelSerializer):

    class Meta:
        model = JobOffer
        fields = '__all__'