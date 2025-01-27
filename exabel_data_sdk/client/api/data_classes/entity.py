from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping, Union

from exabel_data_sdk.client.api.proto_utils import from_struct, to_struct
from exabel_data_sdk.stubs.exabel.api.data.v1.all_pb2 import Entity as ProtoEntity


@dataclass
class Entity:
    r"""
    An entity resource in the Data API.

    Attributes:
        name (str):         The resource name of the entity, for example
                            "entityTypes/entityTypeIdentifier/entities/entityIdentifier" or
                            "entityTypes/namespace1.entityTypeIdentifier/entities/
                            namespace2.entityIdentifier". The namespaces must be empty (being
                            global) or one of the predetermined namespaces the customer has access
                            to. If namespace1 is not empty, it must be equal to namespace2. The
                            entity identifier must match the regex [a-zA-Z][\w-]{0,63}.
        display_name (str): The display name of the entity.
        description (str):  One or more paragraphs of text description.
        properties (Dict):  The properties of this entity.
        read_only (bool):   Whether this resource is read only.
    """

    name: str

    display_name: str

    description: str

    properties: Mapping[str, Union[str, bool, int, float]]

    read_only: bool = False

    @staticmethod
    def from_proto(entity: ProtoEntity) -> Entity:
        """Create an Entity from the given protobuf Entity."""
        return Entity(
            name=entity.name,
            display_name=entity.display_name,
            description=entity.description,
            read_only=entity.read_only,
            properties=from_struct(entity.properties),
        )

    def to_proto(self) -> ProtoEntity:
        """Create a protobuf Entity from this Entity."""
        return ProtoEntity(
            name=self.name,
            display_name=self.display_name,
            description=self.description,
            properties=to_struct(self.properties),
        )
