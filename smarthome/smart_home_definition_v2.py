from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional


class Access(Enum):
    R = "R"
    RW = "RW"
    W = "W"


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
    ANK = "ANK"
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
    BSZ = "BSZ"


class Comm(Enum):
    KNX = "KNX"
    MODBUS = "MODBUS"
    PING = "PING"
    ICAL = "ICAL"
    NTP = "NTP"
    EKEY = "EKEY"
    HTTP = "HTTP"


class DeviceSpecification(Enum):
    POWER_KNX = "PowerKNX"
    STEINEL_TRUE_PR_SENZ = "SteinelTruePräsenz"
    ROLLADEN_MDTKNX = "RolladenMDTKNX"
    ICALBINDING = "ICALBinding"
    NTPBINDING = "NTPBinding"
    LIGHT_KNXLIGHT = "LightKNXlight"
    LIGHT_KNXMIDDLE = "LightKNXMiddle"
    LIGHT_KNXFULL = "LightKNXfull"
    GLASTASTER_KNX = "GlastasterKNX"
    DOOR_EKEY = "DoorEKEY"
    HTTP = "HTTP"
    DOOR_ACCESS_KNX = "DoorAccessKNX"
    DOOR_BELL_HTTP = "DoorBellHTTP"


class Format(Enum):
    VALUE_0F = "%.0f"
    VALUE_1F = "%.1f"
    VALUE_2F = "%.2f"
    ND = "ND"
    VALUE_1_TD_1_TM_1_T_Y_1_T_H_1_T_M = "%1$td.%1$tm.%1$tY %1$tH:%1$tM"


class Function(Enum):
    NTP = "NTP"
    LIGHT = "LIGHT"
    SHUTTER = "SHUTTER"
    SENSOR = "SENSOR"
    PINGDEVICE = "PINGDEVICE"
    CALENDAR = "CALENDAR"
    CONTROLUNIT = "CONTROLUNIT"
    POWER = "POWER"
    DOOR = "DOOR"


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


@dataclass
class IcalConfiguration:
    class Meta:
        name = "ical.configuration"

    bridge: Optional["IcalConfiguration.Bridge"] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )

    @dataclass
    class Bridge:
        url: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            },
        )
        refresh_time: Optional[int] = field(
            default=None,
            metadata={
                "name": "refreshTime",
                "type": "Attribute",
                "required": True,
            },
        )
        username: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            },
        )
        password: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            },
        )
        max_size: Optional[int] = field(
            default=None,
            metadata={
                "name": "maxSize",
                "type": "Attribute",
                "required": True,
            },
        )


class IcalDatetimeUnit(Enum):
    MINUTE = "MINUTE"
    HOUR = "HOUR"
    DAY = "DAY"
    WEEK = "WEEK"


class IcalTextValueType(Enum):
    TEXT = "TEXT"
    REGEX = "REGEX"


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
    FA_ARROWS_UP_DOWN = "fa-arrows-up-down"
    FA_HAND = "fa-hand"
    FA_COMPASS = "fa-compass"
    FA_LOCATION_DOT = "fa-location-dot"
    FA_UP_TO_LINE = "fa-up-to-line"
    FA_DOWN_FROM_LINE = "fa-down-from-line"
    FA_STETHOSCOPE = "fa-stethoscope"
    FA_DROPLET_PERCENT = "fa-droplet-percent"
    FA_WIND = "fa-wind"
    FA_POO = "fa-poo"
    FA_HEAT = "fa-heat"
    FA_CALENDAR_DAY = "fa-calendar-day"
    FA_TOGGLE_ON = "fa-toggle-on"
    FA_QUOTE_LEFT = "fa-quote-left"
    FA_STREET_VIEW = "fa-street-view"
    FA_POWER_OFF = "fa-power-off"
    FA_BAN = "fa-ban"
    FA_TIMER = "fa-timer"
    FA_PLUG = "fa-plug"
    FA_UTILITY_POLE = "fa-utility-pole"


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
        dpt: Optional[str] = field(
            default=None,
            metadata={
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
        dpt: Optional[str] = field(
            default=None,
            metadata={
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
class NtpConfiguration:
    class Meta:
        name = "ntp.configuration"

    thing: Optional["NtpConfiguration.Thing"] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )

    @dataclass
    class Thing:
        hostname: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            },
        )
        refresh_interval: Optional[int] = field(
            default=None,
            metadata={
                "name": "refreshInterval",
                "type": "Attribute",
                "required": True,
            },
        )
        refresh_ntp: Optional[int] = field(
            default=None,
            metadata={
                "name": "refreshNtp",
                "type": "Attribute",
                "required": True,
            },
        )
        server_port: Optional[int] = field(
            default=None,
            metadata={
                "name": "serverPort",
                "type": "Attribute",
            },
        )
        time_zone: Optional[str] = field(
            default=None,
            metadata={
                "name": "timeZone",
                "type": "Attribute",
            },
        )


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


class ThingAuthMode(Enum):
    BASIC = "BASIC"
    BASIC_PREEMPTIVE = "BASIC_PREEMPTIVE"
    TOKEN = "TOKEN"
    DIGEST = "DIGEST"


class ThingCommandMethod(Enum):
    GET = "GET"
    PUT = "PUT"
    POST = "POST"


class ThingContentType(Enum):
    PUT = "PUT"
    POST = "POST"


class ThingProtocol(Enum):
    RARE = "RARE"
    MULTI = "MULTI"
    HOME = "HOME"


class ThingStateMethod(Enum):
    GET = "GET"
    PUT = "PUT"
    POST = "POST"


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
    PERCENT_SIGN_PERCENT_SIGN = "%%"
    PPM = "ppm"
    H_PA = "hPa"
    H = "h"
    W = "W"
    WH = "Wh"
    M_A = "mA"


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
class DoorConfiguration:
    class Meta:
        name = "door.configuration"

    thing: Optional["DoorConfiguration.Thing"] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )

    @dataclass
    class Thing:
        base_url: Optional[str] = field(
            default=None,
            metadata={
                "name": "baseURL",
                "type": "Attribute",
                "required": True,
            },
        )
        timeout: Optional[int] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            },
        )
        refresh: Optional[int] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            },
        )
        buffer_size: int = field(
            default=2048,
            metadata={
                "name": "bufferSize",
                "type": "Attribute",
            },
        )
        delay: Optional[int] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            },
        )
        username: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
        password: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
        auth_mode: Optional[ThingAuthMode] = field(
            default=None,
            metadata={
                "name": "authMode",
                "type": "Attribute",
                "required": True,
            },
        )
        state_method: Optional[ThingStateMethod] = field(
            default=None,
            metadata={
                "name": "stateMethod",
                "type": "Attribute",
                "required": True,
            },
        )
        command_method: Optional[ThingCommandMethod] = field(
            default=None,
            metadata={
                "name": "commandMethod",
                "type": "Attribute",
                "required": True,
            },
        )
        content_type: Optional[ThingContentType] = field(
            default=None,
            metadata={
                "name": "contentType",
                "type": "Attribute",
            },
        )
        ignore_sslerrors: Optional[bool] = field(
            default=None,
            metadata={
                "name": "ignoreSSLErrors",
                "type": "Attribute",
                "required": True,
            },
        )
        strict_error_handling: Optional[bool] = field(
            default=None,
            metadata={
                "name": "strictErrorHandling",
                "type": "Attribute",
                "required": True,
            },
        )


@dataclass
class EkeyConfiguration:
    class Meta:
        name = "ekey.configuration"

    thing: Optional["EkeyConfiguration.Thing"] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )

    @dataclass
    class Thing:
        ip_address: Optional[str] = field(
            default=None,
            metadata={
                "name": "ipAddress",
                "type": "Attribute",
                "required": True,
            },
        )
        port: Optional[int] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            },
        )
        protocol: Optional[ThingProtocol] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            },
        )
        nat_ip: Optional[str] = field(
            default=None,
            metadata={
                "name": "natIp",
                "type": "Attribute",
            },
        )
        delimiter: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
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
class Ical:
    class Meta:
        name = "ical"

    max_events: Optional[int] = field(
        default=None,
        metadata={
            "name": "maxEvents",
            "type": "Attribute",
            "required": True,
        },
    )
    refresh_time: Optional[int] = field(
        default=None,
        metadata={
            "name": "refreshTime",
            "type": "Attribute",
            "required": True,
        },
    )
    datetime_unit: Optional[IcalDatetimeUnit] = field(
        default=None,
        metadata={
            "name": "datetimeUnit",
            "type": "Attribute",
            "required": True,
        },
    )
    datetime_start: Optional[str] = field(
        default=None,
        metadata={
            "name": "datetimeStart",
            "type": "Attribute",
            "required": True,
        },
    )
    datetime_end: Optional[str] = field(
        default=None,
        metadata={
            "name": "datetimeEnd",
            "type": "Attribute",
            "required": True,
        },
    )
    text_event_field: Optional[str] = field(
        default=None,
        metadata={
            "name": "textEventField",
            "type": "Attribute",
            "required": True,
            "pattern": r"SUMMARY|DESCRIPTION|COMMENT|CONTACT|LOCATION",
        },
    )
    text_event_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "textEventValue",
            "type": "Attribute",
            "required": True,
        },
    )
    text_value_type: Optional[IcalTextValueType] = field(
        default=None,
        metadata={
            "name": "textValueType",
            "type": "Attribute",
            "required": True,
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
    meta: Optional["Channel.MetaType"] = field(
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
    unit: Optional[Unit] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    access: Optional[Access] = field(
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
    enable: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    persistence: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
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
    extention: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    channel_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "channel.id",
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
        ical: Optional[Ical] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        ntp: Optional[object] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        ekey: Optional[object] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        http: Optional[object] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        internal: Optional[object] = field(
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
    class MetaType:
        meta_attribute: List["Channel.MetaType.MetaAttribute"] = field(
            default_factory=list,
            metadata={
                "name": "meta.Attribute",
                "type": "Element",
                "min_occurs": 1,
            },
        )

        @dataclass
        class MetaAttribute:
            name: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "required": True,
                },
            )
            value: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "required": True,
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
            "required": True,
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
            "required": True,
        },
    )
    device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "device.name",
            "type": "Attribute",
            "required": True,
        },
    )
    device_specification: Optional[DeviceSpecification] = field(
        default=None,
        metadata={
            "name": "device.specification",
            "type": "Attribute",
        },
    )
    device_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "device.id",
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
    ical_configuration: Optional[IcalConfiguration] = field(
        default=None,
        metadata={
            "name": "ical.configuration",
            "type": "Element",
            "required": True,
        },
    )
    ntp_configuration: Optional[NtpConfiguration] = field(
        default=None,
        metadata={
            "name": "ntp.configuration",
            "type": "Element",
            "required": True,
        },
    )
    ekey_configuration: Optional[EkeyConfiguration] = field(
        default=None,
        metadata={
            "name": "ekey.configuration",
            "type": "Element",
            "required": True,
        },
    )
    door_configuration: Optional[DoorConfiguration] = field(
        default=None,
        metadata={
            "name": "door.configuration",
            "type": "Element",
            "required": True,
        },
    )
