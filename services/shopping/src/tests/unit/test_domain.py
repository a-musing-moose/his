from uuid import uuid4

import pytest

from shopping import domain


def test_description_is_required_for_list_items():
    item = domain.ListItem()
    with pytest.raises(ValueError):
        item.validate()


def test_dict_representation_of_list_items():
    uuid = uuid4()
    description = 'this is a thing'
    item = domain.ListItem({'uuid': uuid, 'description': description})
    data = item.to_primitive()

    assert data['uuid'] == str(uuid)
    assert data['description'] == description
