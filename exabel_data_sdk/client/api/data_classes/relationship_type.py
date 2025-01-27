from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping, Union

from exabel_data_sdk.client.api.proto_utils import from_struct, to_struct
from exabel_data_sdk.stubs.exabel.api.data.v1.all_pb2 import (
    RelationshipType as ProtoRelationshipType,
)


@dataclass
class RelationshipType:
    """
    A relationship type resource in the Data API.

    Attributes:
        name:        The resource name of the relationship type, for example
                     "relationshipTypes/namespace.relationshipTypeIdentifier". The namespace must be
                     empty (being global) or one of the predetermined namespaces the customer has
                     access to. The relationship type identifier must match the regex
                     [A-Z][A-Z0-9_]{0,63}.
        description: One or more paragraphs of text description.
        properties:  The properties of this entity.
        read_only:   Whether this resource is read only.
    """

    name: str

    description: str

    properties: Mapping[str, Union[str, bool, int, float]]

    read_only: bool = False

    @staticmethod
    def from_proto(relationship_type: ProtoRelationshipType) -> RelationshipType:
        """Create a RelationshipType from the given protobuf RelationshipType."""
        return RelationshipType(
            name=relationship_type.name,
            description=relationship_type.description,
            properties=from_struct(relationship_type.properties),
            read_only=relationship_type.read_only,
        )

    def to_proto(self) -> ProtoRelationshipType:
        """Create a protobuf RelationshipType from this RelationshipType."""
        return ProtoRelationshipType(
            name=self.name,
            description=self.description,
            properties=to_struct(self.properties),
        )
