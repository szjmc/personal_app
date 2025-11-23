from rest_framework import serializers
from .models import (
    PackageTracking, PackageStatus, Item, Habit, HabitRecord,
    MealRecord, Transaction, Budget
)


class PackageTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackageTracking
        fields = '__all__'
        read_only_fields = ('id', 'creator', 'created_at', 'updated_at')


class PackageStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackageStatus
        fields = '__all__'
        read_only_fields = ('id', 'created_at')


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
        read_only_fields = ('id', 'creator', 'created_at', 'updated_at', 'is_expired')


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        read_only_fields = ('id', 'creator', 'created_at')


class HabitRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = HabitRecord
        fields = '__all__'
        read_only_fields = ('id', 'created_at')


class MealRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealRecord
        fields = '__all__'
        read_only_fields = ('id', 'creator', 'created_at')


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
        read_only_fields = ('id', 'creator', 'created_at')


class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = '__all__'
        read_only_fields = ('id', 'creator', 'created_at', 'updated_at', 'percentage_used')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = None
        fields = ['id', 'name', 'type', 'description']