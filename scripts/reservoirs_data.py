#!/usr/bin/env python


# This file has been automatically generated.
# Instead of changing it, create a file called import_helper.py
# and put there a class called ImportHelper(object) in it.
#
# This class will be specially casted so that instead of extending object,
# it will actually extend the class BasicImportHelper()
#
# That means you just have to overload the methods you want to
# change, leaving the other ones intact.
#
# Something that you might want to do is use transactions, for example.
#
# Also, don't forget to add the necessary Django imports.
#
# This file was generated with the following command:
# manage.py dumpscript reservoirs
#
# to restore it, run
# manage.py runscript module_name.this_script_name
#
# example: if manage.py is at ./manage.py
# and the script is at ./some_folder/some_script.py
# you must make sure ./some_folder/__init__.py exists
# and run  ./manage.py runscript some_folder.some_script
import os, sys
from django.db import transaction

class BasicImportHelper:

    def pre_import(self):
        pass

    @transaction.atomic
    def run_import(self, import_data):
        import_data()

    def post_import(self):
        pass

    def locate_similar(self, current_object, search_data):
        # You will probably want to call this method from save_or_locate()
        # Example:
        #   new_obj = self.locate_similar(the_obj, {"national_id": the_obj.national_id } )

        the_obj = current_object.__class__.objects.get(**search_data)
        return the_obj

    def locate_object(self, original_class, original_pk_name, the_class, pk_name, pk_value, obj_content):
        # You may change this function to do specific lookup for specific objects
        #
        # original_class class of the django orm's object that needs to be located
        # original_pk_name the primary key of original_class
        # the_class      parent class of original_class which contains obj_content
        # pk_name        the primary key of original_class
        # pk_value       value of the primary_key
        # obj_content    content of the object which was not exported.
        #
        # You should use obj_content to locate the object on the target db
        #
        # An example where original_class and the_class are different is
        # when original_class is Farmer and the_class is Person. The table
        # may refer to a Farmer but you will actually need to locate Person
        # in order to instantiate that Farmer
        #
        # Example:
        #   if the_class == SurveyResultFormat or the_class == SurveyType or the_class == SurveyState:
        #       pk_name="name"
        #       pk_value=obj_content[pk_name]
        #   if the_class == StaffGroup:
        #       pk_value=8

        search_data = { pk_name: pk_value }
        the_obj = the_class.objects.get(**search_data)
        #print(the_obj)
        return the_obj


    def save_or_locate(self, the_obj):
        # Change this if you want to locate the object in the database
        try:
            the_obj.save()
        except:
            print("---------------")
            print("Error saving the following object:")
            print(the_obj.__class__)
            print(" ")
            print(the_obj.__dict__)
            print(" ")
            print(the_obj)
            print(" ")
            print("---------------")

            raise
        return the_obj


importer = None
try:
    import import_helper
    # We need this so ImportHelper can extend BasicImportHelper, although import_helper.py
    # has no knowlodge of this class
    importer = type("DynamicImportHelper", (import_helper.ImportHelper, BasicImportHelper ) , {} )()
except ImportError as e:
    # From Python 3.3 we can check e.name - string match is for backward compatibility.
    if 'import_helper' in str(e):
        importer = BasicImportHelper()
    else:
        raise

import datetime
from decimal import Decimal
from django.contrib.contenttypes.models import ContentType

try:
    import dateutil.parser
    from dateutil.tz import tzoffset
except ImportError:
    print("Please install python-dateutil")
    sys.exit(os.EX_USAGE)

def run():
    importer.pre_import()
    importer.run_import(import_data)
    importer.post_import()

def import_data():
    # Initial Imports

    # Processing model: reservoirs.models.Reservoir

    from reservoirs.models import Reservoir

    reservoirs_reservoir_1 = Reservoir()
    reservoirs_reservoir_1.name = 'Angamuwa Wewa'
    reservoirs_reservoir_1.description = ''
    reservoirs_reservoir_1.division = 'Rajanganaya'
    reservoirs_reservoir_1.capacity = 14400
    reservoirs_reservoir_1.catchment_area = 5000
    reservoirs_reservoir_1.surface_area = 1200
    reservoirs_reservoir_1.created_at = dateutil.parser.parse("2020-08-16T11:53:54.192000+00:00")
    reservoirs_reservoir_1.updated_at = dateutil.parser.parse("2020-08-16T11:53:54.192000+00:00")
    reservoirs_reservoir_1 = importer.save_or_locate(reservoirs_reservoir_1)

    reservoirs_reservoir_2 = Reservoir()
    reservoirs_reservoir_2.name = 'Basawakkulama Wewa'
    reservoirs_reservoir_2.description = ''
    reservoirs_reservoir_2.division = 'N. P. C.'
    reservoirs_reservoir_2.capacity = 1910
    reservoirs_reservoir_2.catchment_area = 1440
    reservoirs_reservoir_2.surface_area = 200
    reservoirs_reservoir_2.created_at = dateutil.parser.parse("2020-08-16T11:52:18.173000+00:00")
    reservoirs_reservoir_2.updated_at = dateutil.parser.parse("2020-08-16T11:52:18.173000+00:00")
    reservoirs_reservoir_2 = importer.save_or_locate(reservoirs_reservoir_2)

    reservoirs_reservoir_3 = Reservoir()
    reservoirs_reservoir_3.name = 'Hurulu Wewa'
    reservoirs_reservoir_3.description = ''
    reservoirs_reservoir_3.division = 'Galenbidunuwewa'
    reservoirs_reservoir_3.capacity = 55000
    reservoirs_reservoir_3.catchment_area = 30800
    reservoirs_reservoir_3.surface_area = 3500
    reservoirs_reservoir_3.created_at = dateutil.parser.parse("2020-08-16T11:54:33.489000+00:00")
    reservoirs_reservoir_3.updated_at = dateutil.parser.parse("2020-08-16T11:54:33.489000+00:00")
    reservoirs_reservoir_3 = importer.save_or_locate(reservoirs_reservoir_3)

    reservoirs_reservoir_4 = Reservoir()
    reservoirs_reservoir_4.name = 'Mahakanadarawa Wewa'
    reservoirs_reservoir_4.description = ''
    reservoirs_reservoir_4.division = 'Mohintale'
    reservoirs_reservoir_4.capacity = 36250
    reservoirs_reservoir_4.catchment_area = 50401
    reservoirs_reservoir_4.surface_area = 3200
    reservoirs_reservoir_4.created_at = dateutil.parser.parse("2020-08-16T11:49:32.788000+00:00")
    reservoirs_reservoir_4.updated_at = dateutil.parser.parse("2020-08-17T19:15:20.783000+00:00")
    reservoirs_reservoir_4 = importer.save_or_locate(reservoirs_reservoir_4)

    reservoirs_reservoir_5 = Reservoir()
    reservoirs_reservoir_5.name = 'Mahavilachchiya Wewa'
    reservoirs_reservoir_5.description = ''
    reservoirs_reservoir_5.division = 'Mahavilachchiya'
    reservoirs_reservoir_5.capacity = 31500
    reservoirs_reservoir_5.catchment_area = 56560
    reservoirs_reservoir_5.surface_area = 2500
    reservoirs_reservoir_5.created_at = dateutil.parser.parse("2020-08-16T11:50:22.228000+00:00")
    reservoirs_reservoir_5.updated_at = dateutil.parser.parse("2020-08-17T17:57:17.017000+00:00")
    reservoirs_reservoir_5 = importer.save_or_locate(reservoirs_reservoir_5)

    reservoirs_reservoir_6 = Reservoir()
    reservoirs_reservoir_6.name = 'Manankattiya Wewa'
    reservoirs_reservoir_6.description = ''
    reservoirs_reservoir_6.division = 'Galenbidunuwewa'
    reservoirs_reservoir_6.capacity = 7600
    reservoirs_reservoir_6.catchment_area = 9520
    reservoirs_reservoir_6.surface_area = 750
    reservoirs_reservoir_6.created_at = dateutil.parser.parse("2020-08-16T11:55:15.314000+00:00")
    reservoirs_reservoir_6.updated_at = dateutil.parser.parse("2020-08-16T11:55:15.314000+00:00")
    reservoirs_reservoir_6 = importer.save_or_locate(reservoirs_reservoir_6)

    reservoirs_reservoir_7 = Reservoir()
    reservoirs_reservoir_7.name = 'Nachchaduwa'
    reservoirs_reservoir_7.description = ''
    reservoirs_reservoir_7.division = 'Nachchaduwa'
    reservoirs_reservoir_7.capacity = 45150
    reservoirs_reservoir_7.catchment_area = 94000
    reservoirs_reservoir_7.surface_area = 3000
    reservoirs_reservoir_7.created_at = dateutil.parser.parse("2020-08-16T11:46:54.878000+00:00")
    reservoirs_reservoir_7.updated_at = dateutil.parser.parse("2020-08-16T11:46:54.878000+00:00")
    reservoirs_reservoir_7 = importer.save_or_locate(reservoirs_reservoir_7)

    reservoirs_reservoir_8 = Reservoir()
    reservoirs_reservoir_8.name = 'Nuwara Wewa'
    reservoirs_reservoir_8.description = ''
    reservoirs_reservoir_8.division = 'N.P.E'
    reservoirs_reservoir_8.capacity = 36050
    reservoirs_reservoir_8.catchment_area = 13000
    reservoirs_reservoir_8.surface_area = 2500
    reservoirs_reservoir_8.created_at = dateutil.parser.parse("2020-08-16T11:48:39.656000+00:00")
    reservoirs_reservoir_8.updated_at = dateutil.parser.parse("2020-08-16T11:48:39.656000+00:00")
    reservoirs_reservoir_8 = importer.save_or_locate(reservoirs_reservoir_8)

    reservoirs_reservoir_9 = Reservoir()
    reservoirs_reservoir_9.name = 'Padaviya'
    reservoirs_reservoir_9.description = ''
    reservoirs_reservoir_9.division = 'Padaviya'
    reservoirs_reservoir_9.capacity = 85000
    reservoirs_reservoir_9.catchment_area = 83200
    reservoirs_reservoir_9.surface_area = 6000
    reservoirs_reservoir_9.created_at = dateutil.parser.parse("2020-08-16T11:43:49.978000+00:00")
    reservoirs_reservoir_9.updated_at = dateutil.parser.parse("2020-08-16T11:44:06.424000+00:00")
    reservoirs_reservoir_9 = importer.save_or_locate(reservoirs_reservoir_9)

    reservoirs_reservoir_10 = Reservoir()
    reservoirs_reservoir_10.name = 'Rajanganaya Wewa'
    reservoirs_reservoir_10.description = ''
    reservoirs_reservoir_10.division = 'Rajanganaya'
    reservoirs_reservoir_10.capacity = 81603
    reservoirs_reservoir_10.catchment_area = 118800
    reservoirs_reservoir_10.surface_area = 4000
    reservoirs_reservoir_10.created_at = dateutil.parser.parse("2020-08-16T11:53:01.154000+00:00")
    reservoirs_reservoir_10.updated_at = dateutil.parser.parse("2020-08-16T11:53:01.154000+00:00")
    reservoirs_reservoir_10 = importer.save_or_locate(reservoirs_reservoir_10)

    reservoirs_reservoir_11 = Reservoir()
    reservoirs_reservoir_11.name = 'Thisawewa'
    reservoirs_reservoir_11.description = ''
    reservoirs_reservoir_11.division = 'N.P.C'
    reservoirs_reservoir_11.capacity = 3500
    reservoirs_reservoir_11.catchment_area = 800
    reservoirs_reservoir_11.surface_area = 350
    reservoirs_reservoir_11.created_at = dateutil.parser.parse("2020-08-16T11:51:11.684000+00:00")
    reservoirs_reservoir_11.updated_at = dateutil.parser.parse("2020-08-16T11:51:11.684000+00:00")
    reservoirs_reservoir_11 = importer.save_or_locate(reservoirs_reservoir_11)

    reservoirs_reservoir_12 = Reservoir()
    reservoirs_reservoir_12.name = 'Thuruwila Wewa'
    reservoirs_reservoir_12.description = ''
    reservoirs_reservoir_12.division = 'Nachchaduwa'
    reservoirs_reservoir_12.capacity = 5190
    reservoirs_reservoir_12.catchment_area = 12000
    reservoirs_reservoir_12.surface_area = 500
    reservoirs_reservoir_12.created_at = dateutil.parser.parse("2020-08-16T11:47:44.351000+00:00")
    reservoirs_reservoir_12.updated_at = dateutil.parser.parse("2020-08-16T11:47:44.351000+00:00")
    reservoirs_reservoir_12 = importer.save_or_locate(reservoirs_reservoir_12)

    reservoirs_reservoir_13 = Reservoir()
    reservoirs_reservoir_13.name = 'Vahalkada'
    reservoirs_reservoir_13.description = ''
    reservoirs_reservoir_13.division = 'Horowpothana / Kebithigollewa'
    reservoirs_reservoir_13.capacity = 43000
    reservoirs_reservoir_13.catchment_area = 12600
    reservoirs_reservoir_13.surface_area = 2500
    reservoirs_reservoir_13.created_at = dateutil.parser.parse("2020-08-16T11:46:21.085000+00:00")
    reservoirs_reservoir_13.updated_at = dateutil.parser.parse("2020-08-16T11:46:21.085000+00:00")
    reservoirs_reservoir_13 = importer.save_or_locate(reservoirs_reservoir_13)

