def on_forever():
    music.play_tone(294, music.beat(BeatFraction.HALF))
    music.play_tone(294, music.beat(BeatFraction.HALF))
    music.play_tone(330, music.beat(BeatFraction.WHOLE))
    music.play_tone(294, music.beat(BeatFraction.WHOLE))
    music.play_tone(392, music.beat(BeatFraction.WHOLE))
    music.play_tone(370, music.beat(BeatFraction.DOUBLE))
    music.play_tone(294, music.beat(BeatFraction.HALF))
    music.play_tone(294, music.beat(BeatFraction.HALF))
    music.play_tone(330, music.beat(BeatFraction.WHOLE))
    music.play_tone(294, music.beat(BeatFraction.WHOLE))
    music.play_tone(440, music.beat(BeatFraction.WHOLE))
    music.play_tone(392, music.beat(BeatFraction.WHOLE))
    music.play_tone(294, music.beat(BeatFraction.HALF))
    music.play_tone(294, music.beat(BeatFraction.HALF))
    music.play_tone(587, music.beat(BeatFraction.WHOLE))
    music.play_tone(494, music.beat(BeatFraction.WHOLE))
    music.play_tone(392, music.beat(BeatFraction.WHOLE))
    music.play_tone(370, music.beat(BeatFraction.WHOLE))
    music.play_tone(523, music.beat(BeatFraction.HALF))
    music.play_tone(523, music.beat(BeatFraction.HALF))
    music.play_tone(494, music.beat(BeatFraction.WHOLE))
    music.play_tone(392, music.beat(BeatFraction.WHOLE))
    music.play_tone(440, music.beat(BeatFraction.WHOLE))
    music.play_tone(392, music.beat(BeatFraction.DOUBLE))
basic.forever(on_forever)

def on_forever2():
    basic.show_leds("""
        . . . . .
                . # . # .
                . # # # .
                . . # . .
                . . . . .
    """)
    basic.show_string("HAPPYBIRTHDAYNANAK")
    basic.show_leds("""
        # # . # #
                # # # # #
                # # # # #
                . # # # .
                . . # . .
    """)
    basic.show_icon(IconNames.HAPPY)
basic.forever(on_forever2)
