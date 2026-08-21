from datetime import datetime


stats = {

    "scans": 0,

    "signals": 0,

    "errors": 0,

    "last_update": None

}



def add_scan():

    stats["scans"] += 1

    stats["last_update"] = (
        datetime.now().isoformat()
    )



def add_signal():

    stats["signals"] += 1



def add_error():

    stats["errors"] += 1



def get_report():

    return stats
