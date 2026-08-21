from database import get_signals



def get_history():

    signals = get_signals()

    history = []


    for signal in signals:

        history.append({

            "id": signal[0],

            "symbol": signal[1],

            "score": signal[2],

            "reasons": signal[3],

            "created_at": signal[4]

        })


    return history
