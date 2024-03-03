# Music Band Documentation

This repository contains a Python program that simulates a music band with members playing different musical instruments. The main classes in this program are `MusicInstrument`, `Guitar`, `Bass`, and `Drums`.

## MusicInstrument Class

The `MusicInstrument` class represents a generic musical instrument and has the following attributes:

- `player`: The name of the player.
- `num_strings`: The number of strings the instrument has.
- `type`: The type of the instrument, which can be either 'acoustic' or 'electric'.

It also has a method `play_it(notes)` that allows the player to play notes. The behavior differs based on the type of the instrument.

## Guitar Class

The `Guitar` class is a subclass of `MusicInstrument` and represents a guitar instrument. It has a method `strum_chords(chords)` that allows the guitarist to strum chords. 

## Bass Class

The `Bass` class is a subclass of `MusicInstrument` and represents a bass guitar instrument. It has a method `play_riff(riff)` that allows the bassist to play a riff.

## Drums Class

The `Drums` class is a subclass of `MusicInstrument` and represents a drum instrument. It has a method `hit_drums(drum_type)` that allows the drummer to hit the drums.

## Band Simulation

In the provided script, an instance of each instrument is created - a guitarist, a bassist, and a drummer. The band then plays a song where each member showcases their unique skills. The guitarist strums chords, the bassist plays a riff, and the drummer hits the drums.

## Usage

To run the simulation, execute the script in the terminal. Here is an example output of the band playing a song:

```
The band is playing a song:
The electric Karl strums ['Am', 'Em', 'Dm'] chords!
The electric Dallas plays a cool bassline riff!
The acoustic George hits the snare drum!

Wow! Each band member showcases their unique skills!
Karl plays fast solo!
Dallas plays slowly funky bassline!
George plays slowly drum solo!
George plays slowly another one drum solo!
```

Feel free to modify the players, instruments, and actions to create your own music band simulation.