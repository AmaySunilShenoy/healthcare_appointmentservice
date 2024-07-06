from rest_framework import generics

class IdentifierLookupMixin:
    def get_object(self):
        queryset = self.get_queryset()
        queryset = self.filter_queryset(queryset)
        filter = {}

        identifier = self.kwargs.get('identifier', None)
        if identifier:
            if identifier.isdigit():
                filter['id'] = int(identifier)
            else:
                filter['email'] = identifier
        else:
            raise ValueError("Identifier not found in kwargs")

        obj = generics.get_object_or_404(queryset, **filter)
        print(obj)
        self.check_object_permissions(self.request, obj)
        return obj
    