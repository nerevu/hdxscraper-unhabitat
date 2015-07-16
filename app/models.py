# -*- coding: utf-8 -*-
"""
    app.models
    ~~~~~~~~~~

    Provides the SQLAlchemy models
"""
from __future__ import (
    absolute_import, division, print_function, with_statement,
    unicode_literals)

import savalidation.validators as val

from datetime import datetime as dt, date as d
from app import db
from savalidation import ValidationMixin


class Data(db.Model, ValidationMixin):
    # auto keys
    id = db.Column(db.Integer, primary_key=True)
    utc_created = db.Column(db.DateTime, nullable=False, default=dt.utcnow())
    utc_updated = db.Column(
        db.DateTime, nullable=False, default=dt.utcnow(), onupdate=dt.utcnow())

    # other keys
    AREA_id = db.Column(db.String(16), nullable=False)
    AREA_value = db.Column(db.String(16), nullable=False)
    OBS_VALUE = db.Column(db.String(16), nullable=False)
    SOURCE = db.Column(db.String(16), nullable=False)
    DENOMINATOR = db.Column(db.String(16), nullable=False)
    UNIT_id = db.Column(db.String(16), nullable=False)
    SUBGROUP_id = db.Column(db.String(16), nullable=False)
    INDICATOR_id = db.Column(db.String(16), nullable=False)
    UNIT_value = db.Column(db.String(16), nullable=False)
    FOOTNOTES = db.Column(db.String(1024), nullable=True)
    SUBGROUP_value = db.Column(db.String(16), nullable=False)
    TIME_PERIOD = db.Column(db.String(16), nullable=False)
    INDICATOR_value = db.Column(db.String(16), nullable=False)

    # validation
    val.validates_constraints()

    def __repr__(self):
        return ('<Data(%r, %r)>' % (self.indicator, self.area))
