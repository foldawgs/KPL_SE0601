from enum import Enum

# STATE BROK INI 
class TrafficLightState(Enum):
    MERAH = "MERAH"
    KUNING = "KUNING"
    HIJAU = "HIJAU"


# KALO INI TRANSITION ATAU PERUBAHAN STATE BROK
state_transition = {
    TrafficLightState.MERAH: TrafficLightState.KUNING,
    TrafficLightState.KUNING: TrafficLightState.HIJAU,
    TrafficLightState.HIJAU: TrafficLightState.MERAH
}

# KALO INI DURASI STATE BROK
state_durations = {
    TrafficLightState.MERAH: 60,
    TrafficLightState.KUNING: 5,
    TrafficLightState.HIJAU: 60,
}

current_state = TrafficLightState.MERAH
# next_state = state_transition[current_state]
# print(f"State sekarang: {current_state}")
# print(f"State selanjutnya: {next_state}")
# print(f"Durasi state: {state_durations[current_state]} detik")

while True:
    next_state = state_transition[current_state]
    print(f"State sekarang: {current_state}")
    print(f"State selanjutnya: {next_state}")
    print(f"Durasi state: {state_durations[current_state]} detik")
    current_state = next_state
    print("")