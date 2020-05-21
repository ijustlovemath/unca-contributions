def funding(efc, base=50, forty_to_zero=True):
    funds = base
    print(f"{base}$ allocated at baseline")
    if efc > 40000:
        return funds
    if True or efc > 35000:
        diff = 40000 - efc
        ticks = diff // 2000
        funds += ticks * 10
        print(f"+{ticks * 10}$ allocated from {ticks} ticks")
    if efc <= 35000:
        diff = 35000 - efc
        ticks = diff // 500
        funds += ticks * 10
        print(f"+{ticks * 10}$ allocated from {ticks} ticks")
    return funds
