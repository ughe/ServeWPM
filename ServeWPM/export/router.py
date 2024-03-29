class ExportRouter(object):
    
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'export':
            return 'export'
        return None

    def db_for_write(self, model, **hints):
        return False

    def allow_relation(self, obj1, obj2, **hints):
        return (obj1._meta.app_label == obj2._meta.app_label == 'export')

    def allow_syncdb(self, db, model):
        return False

