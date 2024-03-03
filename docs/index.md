# Music Band Documentation

This documentation provides an overview of a Python program that simulates a music band with members playing different musical instruments. The band consists of a guitarist, a bassist, and a drummer, each demonstrating their unique skills through playing various musical elements. The program utilizes classes and inheritance to represent different types of musical instruments and their players.

## Classes

### `MusicInstrument`
- This is the base class for all musical instruments.
- **Attributes**:
  - `player`: Represents the player of the instrument.
  - `num_strings`: Indicates the number of strings the instrument has.
  - `type`: Specifies the type of the instrument (default is acoustic).
- **Methods**:
  - `play_it(notes)`: Plays the instrument based on the notes provided.

### `Guitar`
- Inherits from `MusicInstrument` class.
- Represents a guitar player.
- **Additional Methods**:
  - `strum_chords(chords)`: Strums chords on the guitar.

### `Bass`
- Inherits from `MusicInstrument` class.
- Represents a bass guitar player.
- **Additional Methods**:
  - `play_riff(riff)`: Plays a riff on the bass guitar.

### `Drums`
- Inherits from `MusicInstrument` class.
- Represents a drummer.
- **Additional Methods**:
  - `hit_drums(drum_type)`: Hits a specific type of drum.

## Usage

1. Create instances of `Guitar`, `Bass`, and `Drums` classes with respective player names and instrument details.
2. Simulate the band playing a song by calling methods to play chords, riffs, and hit drums.
3. Each band member demonstrates their unique skills through solos and specific musical elements.

```python
from music.music import Guitar, Bass, Drums

guitarist = Guitar("Karl", 6, type='electric')
guitarist_2 = Guitar("Kerry", 6, type='electric')
bassist = Bass("Dallas", 4)
drummer = Drums("George", type='acoustic')

print("The band is playing a song:")
guitarist.strum_chords(["Am", "Em", "Dm"])
guitarist_2.strum_chords(["Dm", "Dm", "Dm"])
bassist.play_riff("bassline")
drummer.hit_drums("snare")

print("\nWow! Each band member showcases their unique skills!")
guitarist.play_it("solo")
guitarist_2.play_it("super solo")
bassist.play_it("funky bassline")
drummer.play_it("drum solo")
```

This documentation provides an insight into how the program models a music band and demonstrates the interactions between band members playing various musical instruments.