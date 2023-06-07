import Game


def find_finest_fields_to_play(ai_bot):
    # Find the finest fields to play
    finest_fields = []
    for i in range(0, len(ai_bot.fields)):
        if ai_bot.fieldCardCount[i] < 3:
            finest_fields.append(ai_bot.fields[i])
    return finest_fields
