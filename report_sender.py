from report import get_report



def build_report_message():

    stats = get_report()


    return f"""
🦅 <b>AriyoAI Daily Report</b>

🔎 Total Scans:
{stats['scans']}

🚨 Signals:
{stats['signals']}

❌ Errors:
{stats['errors']}

⏰ Last Update:
{stats['last_update']}
"""
