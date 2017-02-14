from uuid import uuid4

from schematics.models import Model
from schematics.types import BooleanType, StringType, UUIDType


class ListItem(Model):
    """Represents a single item in the shopping list"""

    uuid = UUIDType(required=True, default=uuid4)
    description = StringType(required=True, max_length=256)
    checked = BooleanType(required=True, default=False)
