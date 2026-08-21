from bot import send_status, send_report



def handle_command(command):

    if command == "/status":

        send_status()

        return True


    if command == "/report":

        send_report()

        return True


    return False
