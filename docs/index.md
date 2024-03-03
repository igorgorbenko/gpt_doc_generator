# Music Band Documentation

This documentation provides an overview of a Python program that simulates a music band with members playing different musical instruments. The instruments include Guitar, Bass, and Drums. Each instrument has specific functionalities to showcase the skills of the band members.

## Classes Overview

### `MusicInstrument`
- The base class for all music instruments.
- **Attributes**:
    - `player`: The name of the player.
    - `num_strings`: The number of strings in the instrument.
    - `type`: The type of the instrument (default is 'acoustic').
- **Methods**:
    - `play_it(notes)`: Plays the instrument based on the notes provided.

### `Guitar`
- Subclass of `MusicInstrument` representing a Guitar.
- **Additional Attributes**:
    - None
- **Additional Methods**:
    - `strum_chords(chords)`: Strums chords on the guitar.

### `Bass`
- Subclass of `MusicInstrument` representing a Bass guitar.
- **Additional Attributes**:
    - None
- **Additional Methods**:
    - `play_riff(riff)`: Plays a riff on the bass guitar.

### `Drums`
- Subclass of `MusicInstrument` representing Drums.
- **Additional Attributes**:
    - None
- **Additional Methods**:
    - `hit_drums(drum_type)`: Hits a specific type of drum.

## Band Setup and Performance

The code sets up a band with the following members:
- **Guitarist**: Karl, playing an electric guitar.
- **Bassist**: Dallas, playing a 4-string bass guitar.
- **Drummer**: George, playing acoustic drums.

The band performs the following actions:
1. **Playing a Song**:
    - Guitarist strums chords: ["Am", "Em", "Dm"]
    - Bassist plays a bassline riff.
    - Drummer hits the snare drum.

2. **Showcasing Skills**:
    - Each band member showcases their unique skills:
        - Guitarist plays a solo.
        - Bassist plays a funky bassline.
        - Drummer performs a drum solo.

### Note
- The band members demonstrate their skills based on the type of instrument they are playing (acoustic or electric).

This documentation outlines the structure and functionality of the Python program simulating a music band, highlighting the interactions between band members and their instruments.