from affinity.core import models

def test_field_value_changes_list(client):
    many = client.lists().list()
    test_list = [l for l in many if "test" in l.name.lower()][0]
    fields = client.fields().list(list_id=test_list.id)
    status_field = [i for i in fields if i.name == "Status"][0]
    field_value_changes = client.field_value_changes().list(field_id=status_field.id)
    assert isinstance(field_value_changes[0], models.FieldValueChange)

