from __future__ import annotations
from dataclasses import dataclass
from typing import Callable, Dict

@dataclass(frozen=True)
class SensorEntityDescription:
    """Beschreibung eines Sensors."""
    key: str
    translation_key: str
    native_unit_of_measurement: str
    device_class: str
    state_class: str
    entity_category: str
    icon: str
    exists_fn: Callable[[Dict], bool]
    value_fn: Callable[[Dict], float]

# Beispiel für Sensorbeschreibungen
SENSORS = [
    SensorEntityDescription(
        key="wifi_rssi",
        translation_key="wifi_rssi",
        native_unit_of_measurement="dBm",
        device_class="signal_strength",
        state_class="measurement",
        entity_category="diagnostic",
        icon="mdi:access-point-network",
        exists_fn=lambda device: "wifiRSSI" in device,
        value_fn=lambda device: device["wifiRSSI"]
    ),
    SensorEntityDescription(
        key="sw_version",
        translation_key="sw_version",
        native_unit_of_measurement="version",
        device_class="chip",
        state_class="diagnostic",
        entity_category="diagnostic",
        icon="mdi:chip",
        exists_fn=lambda device: "sw" in device,
        value_fn=lambda device: device["sw"]
    ),
    SensorEntityDescription(
        key="temperature",
        translation_key="temperature",
        native_unit_of_measurement="°C",
        device_class="temperature",
        state_class="measurement",
        entity_category="diagnostic",
        icon="mdi:thermometer",
        exists_fn=lambda device: "temperature" in device,
        value_fn=lambda device: device["temperature"]
    ),
    SensorEntityDescription(
        key="humidity",
        translation_key="humidity",
        native_unit_of_measurement="%",
        device_class="humidity",
        state_class="measurement",
        entity_category="diagnostic",
        icon="mdi:water-percent",
        exists_fn=lambda device: "humidity" in device,
        value_fn=lambda device: device["humidity"]
    ),
    SensorEntityDescription(
        key="co",
        translation_key="co",
        native_unit_of_measurement="ppm",
        device_class="carbon_monoxide",
        state_class="measurement",
        entity_category="diagnostic",
        icon="mdi:gas-cylinder",
        exists_fn=lambda device: "coPpm" in device,
        value_fn=lambda device: device["coPpm"]
    ),
]

# Hilfsfunktion, die alle vorhandenen Sensoren für ein Gerät extrahiert
def get_sensors_for_device(device: Dict) -> list:
    """Gibt eine Liste der Sensoren zurück, die für ein Gerät vorhanden sind."""
    return [
        sensor for sensor in SENSORS if sensor.exists_fn(device)
    ]
