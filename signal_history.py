from datetime import datetime


history = []


def save_history(symbol, score):

    record = {

        "symbol": symbol,

        "score": score,

        "time": datetime.now().isoformat()

    }

    history.append(record)



def get_history():

    return history
