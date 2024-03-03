from music.music import Guitar, Bass, Drums

guitarist = Guitar("Karl", 6, type='electric')
bassist = Bass("Dallas", 4)
drummer = Drums("George", type='acoustic')

print("The band is playing a song:")
guitarist.strum_chords(["Am", "Em", "Dm"])
bassist.play_riff("bassline")
drummer.hit_drums("snare")

print("\nWow! Each band member showcases their unique skills!")
guitarist.play_it("solo")
bassist.play_it("funky bassline")
drummer.play_it("drum solo")
drummer.play_it("another one drum solo")

