import pytest
from sqlalchemy.exc import IntegrityError

from app.models.property import Property


def test_create_property_success(db, agent, user):
    property = Property(
        name="casa do morro", address="Rua 1", agent_id=agent.id, user_id=user.id
    )

    db.add(property)
    db.commit()
    db.refresh(property)

    assert property.id is not None
    assert property.agent_id == agent.id
    assert property.user_id == user.id


def test_create_property_without_agent_should_fail(db, user):
    property = Property(
        name="casa do morro", address="rua 1", agent_id=999, user_id=user.id
    )

    db.add(property)

    with pytest.raises(IntegrityError):
        db.commit()
