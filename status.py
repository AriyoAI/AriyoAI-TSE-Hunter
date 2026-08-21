from health_check import system_health
from report import get_report
from analytics import get_signal_stats



def get_system_status():

    health = system_health()

    report = get_report()

    analytics = get_signal_stats()


    return {

        "health": health,

        "scans": report["scans"],

        "signals": report["signals"],

        "stored_signals": analytics["total"],

        "average_score": analytics["average_score"]

    }
