"""Utility functions and consts."""

from sqlalchemy import inspect

from . import exc
from .sqltypes import FSMField

def is_valid_fsm_state(value):
    return isinstance(value, basestring) and value

def get_fsm_column(table_class):
    fsm_fields = [c for c in inspect(table_class).columns if isinstance(c.type, FSMField)]

    if len(fsm_fields) == 0:
        raise exc.SetupError('No FSMField found in model')
    elif len(fsm_fields) > 1:
        raise exc.SetupError('More than one FSMField found in model ({})'.format(fsm_fields))
    return fsm_fields[0]