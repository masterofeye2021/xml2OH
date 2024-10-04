from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional


class Access(Enum):
    R = "R"
    RW = "RW"


class AlexaInverted(Enum):
    TRUE = "true"
    FALSE = "false"


class Area(Enum):
    WOZ = "WOZ"
    KUE = "KUE"
    HWR = "HWR"
    GWC = "GWC"
    FLUEG = "FLUEG"
    BUR = "BUR"
    SLZ = "SLZ"
    BAD = "BAD"
    KIZ = "KIZ"
    FLUDG = "FLUDG"
    DCH = "DCH"
    TKR = "TKR"
    FLUKL = "FLUKL"
    LAG = "LAG"
    GAR = "GAR"
    CAR = "CAR"
    VALUE = ""


class Comm(Enum):
    KNX = "KNX"
    MODBUS = "MODBUS"
    PING = "PING"


class Format(Enum):
    VALUE_0F = "%.0f"
    VALUE_1F = "%.1f"
    VALUE_2F = "%.2f"
    ND = "ND"


class Function(Enum):
    LIGHT = "LIGHT"
    SHUTTER = "SHUTTER"
    SENSOR = "SENSOR"
    PINGDEVICE = "PINGDEVICE"


class GroupFunction(Enum):
    EQUALITY = "EQUALITY"
    AND = "AND"
    OR = "OR"
    NAND = "NAND"
    NOR = "NOR"
    SUM = "SUM"
    AVG = "AVG"
    MIN = "MIN"
    MAX = "MAX"
    COUNT = "COUNT"
    LATEST = "LATEST"
    EARLIEST = "EARLIEST"


class Icon(Enum):
    FA_LIGHTBULB = "fa-lightbulb"
    FA_BLINDS = "fa-blinds"
    FA_RADAR = "fa-radar"
    FA_TEMPERATURE_THREE_QUARTERS = "fa-temperature-three-quarters"
    FA_CLOUD = "fa-cloud"
    FA_DROPLET = "fa-droplet"
    FA_SIGNAL = "fa-signal"
    FA_OCTAGON = "fa-octagon"
    FA_LOCK = "fa-lock"


@dataclass
class KnxAddress:
    class Meta:
        name = "knx.address"

    main_ga: Optional["KnxAddress.MainGa"] = field(
        default=None,
        metadata={
            "name": "main.ga",
            "type": "Element",
            "required": True,
        },
    )
    listening_ga: Optional["KnxAddress.ListeningGa"] = field(
        default=None,
        metadata={
            "name": "listening.ga",
            "type": "Element",
        },
    )

    @dataclass
    class MainGa:
        main: Optional[int] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )
        middle: Optional[int] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )
        sub: Optional[int] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )
        is_readable: bool = field(
            default=False,
            metadata={
                "name": "is.readable",
                "type": "Attribute",
            },
        )

    @dataclass
    class ListeningGa:
        main: Optional[int] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )
        middle: Optional[int] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )
        sub: Optional[int] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )
        is_readable: bool = field(
            default=True,
            metadata={
                "name": "is.readable",
                "type": "Attribute",
            },
        )


@dataclass
class KnxConfiguration:
    class Meta:
        name = "knx.configuration"

    bridge: Optional["KnxConfiguration.Bridge"] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    tunnel: Optional["KnxConfiguration.Tunnel"] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )

    @dataclass
    class Bridge:
        type_value: str = field(
            default="TUNNEL",
            metadata={
                "name": "type",
                "type": "Attribute",
            },
        )
        ip_address: Optional[str] = field(
            default=None,
            metadata={
                "name": "ip.address",
                "type": "Attribute",
            },
        )
        port_number: str = field(
            default="3671",
            metadata={
                "name": "port.number",
                "type": "Attribute",
            },
        )
        local_ip: Optional[str] = field(
            default=None,
            metadata={
                "name": "local.ip",
                "type": "Attribute",
            },
        )
        reading_pause: int = field(
            default=50,
            metadata={
                "name": "reading.pause",
                "type": "Attribute",
            },
        )
        response_timeout: int = field(
            default=10,
            metadata={
                "name": "response.timeout",
                "type": "Attribute",
            },
        )
        read_retries_limit: int = field(
            default=3,
            metadata={
                "name": "read.retries.limit",
                "type": "Attribute",
            },
        )
        auto_reconnect_period: int = field(
            default=60,
            metadata={
                "name": "auto.reconnect.period",
                "type": "Attribute",
            },
        )

    @dataclass
    class Tunnel:
        address: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
        fetch: bool = field(
            default=True,
            metadata={
                "type": "Attribute",
            },
        )
        ping_interval: int = field(
            default=300,
            metadata={
                "name": "ping.interval",
                "type": "Attribute",
            },
        )
        read_interval: int = field(
            default=3600,
            metadata={
                "name": "read.interval",
                "type": "Attribute",
            },
        )


class ModbusReadValue(Enum):
    UINT16 = "uint16"
    INT32 = "int32"
    UINT32 = "uint32"


class ModbusType(Enum):
    HOLDING = "holding"


@dataclass
class Ping:
    class Meta:
        name = "ping"

    ip: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    mac: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


class TypeValue(Enum):
    SWITCH = "Switch"
    NUMBER = "Number"
    ROLLERSHUTTER = "Rollershutter"
    CONTACT = "Contact"
    DATE_TIME = "DateTime"
    STRING = "String"
    DIMMER = "Dimmer"


class Unit(Enum):
    ND = "ND"
    C = "°C"
    K = "K"
    U = "U"
    I = "I"
    PERCENT_SIGN = "%"


@dataclass
class Alexa:
    class Meta:
        name = "alexa"

    inverted: Optional[AlexaInverted] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    primary_control: Optional[str] = field(
        default=None,
        metadata={
            "name": "primaryControl",
            "type": "Attribute",
        },
    )
    capability_names: Optional[str] = field(
        default=None,
        metadata={
            "name": "capabilityNames",
            "type": "Attribute",
        },
    )
    supported_commands: Optional[str] = field(
        default=None,
        metadata={
            "name": "supportedCommands",
            "type": "Attribute",
        },
    )
    supported_range: Optional[str] = field(
        default=None,
        metadata={
            "name": "supportedRange",
            "type": "Attribute",
        },
    )
    unit_of_measure: Optional[str] = field(
        default=None,
        metadata={
            "name": "unitOfMeasure",
            "type": "Attribute",
        },
    )
    action_mappings: Optional[str] = field(
        default=None,
        metadata={
            "name": "actionMappings",
            "type": "Attribute",
        },
    )
    state_mappings: Optional[str] = field(
        default=None,
        metadata={
            "name": "stateMappings",
            "type": "Attribute",
        },
    )
    alexa: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Group:
    class Meta:
        name = "group"

    group_ref: List["Group.GroupRef"] = field(
        default_factory=list,
        metadata={
            "name": "group.ref",
            "type": "Element",
        },
    )
    type_value: Optional[TypeValue] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
    label: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    icon: Optional[Icon] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    function: Optional[GroupFunction] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass
    class GroupRef:
        refid: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )


@dataclass
class Knx:
    class Meta:
        name = "knx"

    add1: Optional[KnxAddress] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    add2: Optional[KnxAddress] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    add3: Optional[KnxAddress] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Modbus:
    class Meta:
        name = "modbus"

    poller: Optional["Modbus.Poller"] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    address: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    read_value: Optional[ModbusReadValue] = field(
        default=None,
        metadata={
            "name": "read.value",
            "type": "Element",
            "required": True,
        },
    )

    @dataclass
    class Poller:
        address: Optional[int] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )
        length: Optional[int] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )
        type_value: ModbusType = field(
            default=ModbusType.HOLDING,
            metadata={
                "name": "type",
                "type": "Element",
                "required": True,
            },
        )


@dataclass
class Channel:
    class Meta:
        name = "channel"

    link: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    connection: Optional["Channel.Connection"] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    groups: Optional["Channel.Groups"] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    alexa: Optional[Alexa] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    format: Optional[Format] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    unit: Unit = field(
        default=Unit.ND,
        metadata={
            "type": "Attribute",
        },
    )
    access: Optional[Access] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    icon: Optional[Icon] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    enable: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    persistence: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    label: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    type_value: Optional[TypeValue] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    extention: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )

    @dataclass
    class Connection:
        knx: Optional[Knx] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        ping: Optional[Ping] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        modbus: Optional[Modbus] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )

    @dataclass
    class Groups:
        group_ref: List["Channel.Groups.GroupRef"] = field(
            default_factory=list,
            metadata={
                "name": "group.ref",
                "type": "Element",
                "min_occurs": 1,
            },
        )

        @dataclass
        class GroupRef:
            refid: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                },
            )


@dataclass
class Groups:
    class Meta:
        name = "groups"

    group: List[Group] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class Device:
    class Meta:
        name = "device"

    channel: List[Channel] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    device_area: Optional[Area] = field(
        default=None,
        metadata={
            "name": "device.area",
            "type": "Attribute",
        },
    )
    device_function: Optional[Function] = field(
        default=None,
        metadata={
            "name": "device.function",
            "type": "Attribute",
        },
    )
    device_comm_type: Comm = field(
        default=Comm.KNX,
        metadata={
            "name": "device.comm.type",
            "type": "Attribute",
        },
    )
    device_label: Optional[str] = field(
        default=None,
        metadata={
            "name": "device.label",
            "type": "Attribute",
        },
    )
    device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "device.name",
            "type": "Attribute",
        },
    )


@dataclass
class Devices:
    class Meta:
        name = "devices"

    device: List[Device] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class Openhab:
    """
    Comment describing your root element.
    """

    class Meta:
        name = "openhab"

    devices: Optional[Devices] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    groups: Optional[Groups] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    knx_configuration: Optional[KnxConfiguration] = field(
        default=None,
        metadata={
            "name": "knx.configuration",
            "type": "Element",
            "required": True,
        },
    )
