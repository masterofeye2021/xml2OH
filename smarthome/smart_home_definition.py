from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional


class Area(Enum):
    WOZ = "WOZ"
    KUE = "KUE"
    HWR = "HWR"
    GWC = "GWC"
    FLUEG = "FLUEG"


class Channel(Enum):
    KNX = "KNX"
    MODBUS = "MODBUS"
    EKEY = "EKEY"


class Format(Enum):
    VALUE_0F = "%.0f"
    VALUE_1F = "%.1f"
    VALUE_2F = "%.2f"
    ND = "ND"


class Function(Enum):
    LIGHT = "Light"
    HEALTH = "Health"
    SHUTTER = "Shutter"
    SENSOR = "Sensor"
    PHOTOVOLTAICS = "Photovoltaics"
    HEATING = "Heating"


@dataclass
class ItemLink:
    link: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


class Read(Enum):
    R = "R"
    RW = "RW"


class SensorType(Enum):
    TEMPERATUR = "Temperatur"
    FEUCHTIGKEIT = "Feuchtigkeit"
    CO2 = "Co2"


class Unit(Enum):
    C = "°C"
    K = "K"
    U = "U"
    I = "I"
    PERCENT_SIGN = "%"


@dataclass
class Item:
    tags: Optional["Item.Tags"] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    item_link: Optional[ItemLink] = field(
        default=None,
        metadata={
            "name": "item.link",
            "type": "Element",
            "required": True,
        },
    )
    enable: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    icon: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    unit: Optional[Unit] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    format: Format = field(
        default=Format.VALUE_1F,
        metadata={
            "type": "Attribute",
        },
    )
    function: Optional[Function] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    channel: Channel = field(
        default=Channel.KNX,
        metadata={
            "type": "Attribute",
        },
    )
    read: Optional[Read] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    assignment: Optional[Area] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass
    class Tags:
        replacer_tag: Optional[str] = field(
            default=None,
            metadata={
                "name": "replacerTag",
                "type": "Element",
                "required": True,
            },
        )


@dataclass
class Health:
    item_link: Optional[ItemLink] = field(
        default=None,
        metadata={
            "name": "Item.link",
            "type": "Element",
            "required": True,
        },
    )
    online: Optional[Item] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    last_seen: Optional[Item] = field(
        default=None,
        metadata={
            "name": "last.seen",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Light:
    on: Optional[Item] = field(
        default=None,
        metadata={
            "name": "On",
            "type": "Element",
            "required": True,
        },
    )
    off: Optional[Item] = field(
        default=None,
        metadata={
            "name": "Off",
            "type": "Element",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Photovoltaik:
    self_consumption: Optional[Item] = field(
        default=None,
        metadata={
            "name": "self.consumption",
            "type": "Element",
            "required": True,
        },
    )
    energy_production: Optional[Item] = field(
        default=None,
        metadata={
            "name": "energy.production",
            "type": "Element",
            "required": True,
        },
    )
    energy_consumption: Optional[Item] = field(
        default=None,
        metadata={
            "name": "energy.consumption",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Rollladen:
    up: Optional[Item] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    down: Optional[Item] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    stop: Optional[Item] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    direction: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    status_top: Optional[bool] = field(
        default=None,
        metadata={
            "name": "statusTop",
            "type": "Attribute",
        },
    )
    status_bottom: Optional[bool] = field(
        default=None,
        metadata={
            "name": "statusBottom",
            "type": "Attribute",
        },
    )
    absolut_position: Optional[int] = field(
        default=None,
        metadata={
            "name": "absolutPosition",
            "type": "Attribute",
        },
    )


@dataclass
class Sensor:
    measurement: Optional[Item] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    sensor_type: Optional[SensorType] = field(
        default=None,
        metadata={
            "name": "sensorType",
            "type": "Attribute",
        },
    )
    assignment: Optional[Area] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class SystemAir:
    ventilation_intensity_read: Optional[Item] = field(
        default=None,
        metadata={
            "name": "ventilation.intensity.read",
            "type": "Element",
            "required": True,
        },
    )
    ventilation_intensity_write: Optional[Item] = field(
        default=None,
        metadata={
            "name": "ventilation.intensity.write",
            "type": "Element",
            "required": True,
        },
    )
    operation_mode_read: Optional[Item] = field(
        default=None,
        metadata={
            "name": "operation.mode.read",
            "type": "Element",
            "required": True,
        },
    )
    operation_mode_write: Optional[Item] = field(
        default=None,
        metadata={
            "name": "operation.mode.write",
            "type": "Element",
            "required": True,
        },
    )
    supply_air_temperature: Optional[Item] = field(
        default=None,
        metadata={
            "name": "supply.air.temperature",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Openhab:
    lights: Optional["Openhab.Lights"] = field(
        default=None,
        metadata={
            "name": "Lights",
            "type": "Element",
            "required": True,
        },
    )
    shutter: List[Rollladen] = field(
        default_factory=list,
        metadata={
            "name": "Shutter",
            "type": "Element",
        },
    )
    sensors: List[Sensor] = field(
        default_factory=list,
        metadata={
            "name": "Sensors",
            "type": "Element",
        },
    )
    home_ventilation: Optional[SystemAir] = field(
        default=None,
        metadata={
            "name": "HomeVentilation",
            "type": "Element",
            "required": True,
        },
    )
    health_system: Optional[Health] = field(
        default=None,
        metadata={
            "name": "Health.System",
            "type": "Element",
            "required": True,
        },
    )

    @dataclass
    class Lights:
        light: List[Light] = field(
            default_factory=list,
            metadata={
                "name": "Light",
                "type": "Element",
                "min_occurs": 1,
            },
        )
