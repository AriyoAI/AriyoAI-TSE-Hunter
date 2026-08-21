from database import get_signals



def get_signal_stats():

    signals = get_signals()


    total = len(signals)


    if total == 0:

        return {

            "total": 0,

            "average_score": 0

        }


    scores = [
        signal[2]
        for signal in signals
    ]


    average = sum(scores) / total


    return {

        "total": total,

        "average_score": round(
            average,
            2
        )

    }
