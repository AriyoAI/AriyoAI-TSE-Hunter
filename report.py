from datetime import datetime


stats = {

    "scans": 0,

    "signals": 0,

    "errors": 0,

    "last_update": None

}



def update_time():

    stats["last_update"] = (
        datetime.now().isoformat()
    )



def add_scan():

    stats["scans"] += 1

    update_time()



def add_signal():

    stats["signals"] += 1

    update_time()



def add_error():

    stats["errors"] += 1

    update_time()



def get_report():

    return {

        "scans": stats["scans"],

        "signals": stats["signals"],

        "errors": stats["errors"],

        "last_update": stats["last_update"]

    }
