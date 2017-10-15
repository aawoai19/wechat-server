#coding=utf-8

from django.core.management.base import BaseCommand, CommandError
from lundong.shenhu300_chuangyeban import save_data

class Command(BaseCommand):
    help = 'Save data everyday'

    def handle(self, *args, **options):
        save_data()