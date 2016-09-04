from django.db.models import ForeignKey


class CatalogFK(ForeignKey):
    """
    Una buena abstraccion para crear foreignkey a estos modelos.
    No se olvida de que hay que usar el campo "code" preferentemente y no el
      campo ID. Esto nos viene bien para migrar de una base de datos a otra,
      si la operacion es relevante.
    """

    def __init__(self, to, *args, **kwargs):
        kwargs.pop('to_field', None)
        super(CatalogFK, self).__init__(to, to_field='code', *args, **kwargs)