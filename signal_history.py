from database import (
    get_signals,
    save_signal
)



def save_history(symbol, score):

    save_signal(
        symbol,
        score,
        "Signal history saved"
    )



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
