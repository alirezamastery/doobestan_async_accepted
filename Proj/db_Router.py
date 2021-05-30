class HospRouter:
    """
    A router to control all database operations on 'Hospital' and 'Sick' models
    """
    # route_app_labels = {'Hospital', 'contenttypes'}
    route_model_names = {'Hospital', 'Sick'}

    def db_for_read(self, model, **hints):
        """
        Attempts to read 'Hospital' and 'Sick' models go to hospitals.
        """
        # if model._meta.app_label in self.route_app_labels:
        #     return 'auth_db'
        if model.__name__ in self.route_model_names:
            return 'hospitals'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write 'Hospital' and 'Sick' models go to hospitals.
        """
        # if model._meta.app_label in self.route_app_labels:
        #     return 'auth_db'
        if model.__name__ in self.route_model_names:
            return 'hospitals'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model of 'Hospital' and 'Sick' is
        involved.
        """
        # if (
        #         obj1._meta.app_label in self.route_app_labels or
        #         obj2._meta.app_label in self.route_app_labels
        # ):
        #     return True
        if (
                obj1._meta.model.__name__ in self.route_model_names or
                obj2._meta.model.__name__ in self.route_model_names
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the 'Hospital' and 'Sick' models only appear in the
        'hospitals' database.
        """
        # if app_label in self.route_app_labels:
        #     return db == 'auth_db'
        if model_name in self.route_model_names:
            return db == 'hospitals'
        return None


class CompRouter:
    """
    A router to control all database operations on 'Company' and 'Employee' models
    """
    route_model_names = {'Company', 'Employee'}

    def db_for_read(self, model, **hints):
        """
        Attempts to read 'Company' and 'Employee' models go to companies.
        """
        if model.__name__ in self.route_model_names:
            return 'companies'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write 'Company' and 'Employee' models go to companies.
        """
        if model.__name__ in self.route_model_names:
            return 'companies'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model of 'Company' and 'Employee' is involved.
        """
        if (
                obj1._meta.model.__name__ in self.route_model_names or
                obj2._meta.model.__name__ in self.route_model_names
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the 'Company' and 'Employee' models only appear in the
        'companies' database.
        """
        if model_name in self.route_model_names:
            return db == 'companies'
        return None
