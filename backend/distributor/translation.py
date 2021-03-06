from modeltranslation.translator import translator, TranslationOptions
from .models import Measure, NeedType, Donation, Hospital, Region, District, Locality, Statistic, StatisticCategory


class MeasureTranslationOptions(TranslationOptions):
    fields = ('name',)


translator.register(Measure, MeasureTranslationOptions)


class NeedTypeTranslationOptions(TranslationOptions):
    fields = ('name',)


translator.register(NeedType, NeedTypeTranslationOptions)


class DonationTranslationOptions(TranslationOptions):
    fields = ('description', 'donator_name')


translator.register(Donation, DonationTranslationOptions)


class HospitalTranslationOptions(TranslationOptions):
    fields = ('name',)


translator.register(Hospital, HospitalTranslationOptions)


class RegionTranslationOptions(TranslationOptions):
    fields = ('name',)


translator.register(Region, RegionTranslationOptions)


class DistrictTranslationOptions(TranslationOptions):
    fields = ('name',)


translator.register(District, DistrictTranslationOptions)


class LocalityTranslationOptions(TranslationOptions):
    fields = ('name',)


translator.register(Locality, LocalityTranslationOptions)


class StatisticCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


translator.register(StatisticCategory, StatisticCategoryTranslationOptions)
