# Music Band Documentation

This documentation provides an overview of a Python program that simulates a music band consisting of members playing different musical instruments. The code defines classes for various musical instruments like Guitar, Bass, and Drums, along with their functionalities.

## Classes

### `MusicInstrument`
- This is the base class for all musical instruments.
- Attributes:
  - `player`: Represents the player of the instrument.
  - `num_strings`: Indicates the number of strings the instrument has.
  - `type`: Specifies the type of the instrument, default is 'acoustic'.
- Methods:
  - `play_it(notes)`: Plays the instrument based on the type. Slow for acoustic, fast for others.

### `Guitar`
- Subclass of `MusicInstrument` representing a Guitar.
- Additional Methods:
  - `strum_chords(chords)`: Allows the player to strum chords on the guitar.

### `Bass`
- Subclass of `MusicInstrument` representing a Bass guitar.
- Additional Methods:
  - `play_riff(riff)`: Enables the player to play a cool riff on the bass guitar.

### `Drums`
- Subclass of `MusicInstrument` representing Drums.
- Additional Methods:
  - `hit_drums(drum_type)`: Lets the player hit a specific type of drum.

## Band Members

1. **Guitarist**
   - **Name**: Karl
   - **Instrument**: Electric Guitar with 6 strings
   - **Actions**:
     - Strums chords: ["Am", "Em", "Dm"]
     - Plays a solo

2. **Bassist**
   - **Name**: Dallas
   - **Instrument**: Bass Guitar with 4 strings
   - **Actions**:
     - Plays a bassline riff
     - Plays a funky bassline

3. **Drummer**
   - **Name**: George
   - **Instrument**: Acoustic Drums
   - **Actions**:
     - Hits the snare drum
     - Performs a drum solo

## Band Performance

The band comes together to play a song where each member showcases their unique skills. The guitarist strums chords, the bassist plays a riff, and the drummer hits the drums. Following this, each member demonstrates their individual talent through a solo performance.

This Python program exemplifies the coordination and synergy among band members, highlighting their musical expressions and contributions to the overall performance.