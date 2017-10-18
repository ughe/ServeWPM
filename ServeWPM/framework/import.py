# import os
# from dateutil import parser
# from shutil import copyfile, copytree
# from django.db import transaction
# """
# [1] for each folder
#     [2] for each folder
#         [3] copy to tmp.sqlite and tmp.log
#             [4] import
#         [5] mv to archives
# """  

# def migrateTests():
#     for test in os.listdir(path):
#         if os.path.isdir(path + '/' + test):
#             for date in os.listdir(path + '/' + test):
#                 tp = '{}/{}/{}'.format(path, test, date)
#                 copyfile(tp + '/crawl-data.sqlite', path + 'tmp.sqlite')
#                 copyfile(tp + '/openwpm.log', path + '/tmp.log')
#                 log = None
#                 with open(tp + '/openwpm.log', 'r') as logFile:
#                     log = logFile.read()
#                 if (import_file(date, test, log)):
#                     copytree(tp, '{}/../archives/{}/{}'.format(path, test, date))
#                     os.remove(tp)
#                 else:
#                     print "framework.imports: Error failed import"


# def import_file(d, n, l):
#     with transaction.atomic():
#         tg = TestGroup(date=parser.parse(d.replace('\\', ''), name=n, log=l)
#         tg.save(using='default')
#         for m in __all__:
#             for o in m.objects.all()
#                 o.pk = None
#                 try:
#                     o.id = None
#                 except:
#                     pass
#                 o.test_group = tg
#                 o.save(using='default')
            
#         Model.
#         return True
#     except IntegrityError:
#         return False

# if '__name__' == '__main__':
#     migrateTests()

