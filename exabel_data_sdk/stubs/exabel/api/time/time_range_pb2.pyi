# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from typing import Optional as typing___Optional

from google.protobuf.descriptor import Descriptor as google___protobuf___descriptor___Descriptor
from google.protobuf.descriptor import (
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)
from google.protobuf.message import Message as google___protobuf___message___Message
from google.protobuf.timestamp_pb2 import Timestamp as google___protobuf___timestamp_pb2___Timestamp
from typing_extensions import Literal as typing_extensions___Literal

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class TimeRange(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    exclude_from: builtin___bool = ...
    include_to: builtin___bool = ...
    @property
    def from_time(self) -> google___protobuf___timestamp_pb2___Timestamp: ...
    @property
    def to_time(self) -> google___protobuf___timestamp_pb2___Timestamp: ...
    def __init__(
        self,
        *,
        from_time: typing___Optional[google___protobuf___timestamp_pb2___Timestamp] = None,
        exclude_from: typing___Optional[builtin___bool] = None,
        to_time: typing___Optional[google___protobuf___timestamp_pb2___Timestamp] = None,
        include_to: typing___Optional[builtin___bool] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal["from_time", b"from_time", "to_time", b"to_time"],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "exclude_from",
            b"exclude_from",
            "from_time",
            b"from_time",
            "include_to",
            b"include_to",
            "to_time",
            b"to_time",
        ],
    ) -> None: ...

type___TimeRange = TimeRange