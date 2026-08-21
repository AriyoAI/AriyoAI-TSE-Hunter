from bot import send_message



def send_error_alert(error):

    message = f"""
🚨 <b>AriyoAI System Alert</b>

❌ خطا در اجرای سیستم:

{error}
"""

    send_message(message)
