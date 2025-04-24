from enum import Enum

class FSM(Enum):
    IDLE = "Idle"
    MENUNGGUPRODUK = "MenungguProduk"
    MENGELUARKANPRODUK = "MengeluarkanProduk"
    SELESAI = "Selesai"

state_transition = {
    FSM.IDLE: FSM.MENUNGGUPRODUK,
    FSM.MENUNGGUPRODUK: FSM.MENGELUARKANPRODUK,
    FSM.MENGELUARKANPRODUK: FSM.SELESAI,
    FSM.SELESAI: FSM.IDLE,
}

state_durations = {
    FSM.IDLE: 1,
    FSM.MENUNGGUPRODUK: 1,
    FSM.MENGELUARKANPRODUK: 1,
    FSM.SELESAI: 1,
}

