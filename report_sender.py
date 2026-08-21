from report import get_report

from analytics import get_signal_stats



def build_report_message():

    stats = get_report()

    signal_stats = get_signal_stats()


    return f"""
🦅 <b>AriyoAI Daily Report</b>


🔎 Total Scans:
{stats['scans']}


🚨 Signals:
{stats['signals']}


📊 Stored Signals:
{signal_stats['total']}


⭐ Average Score:
{signal_stats['average_score']}


❌ Errors:
{stats['errors']}


⏰ Last Update:
{stats['last_update']}
"""
