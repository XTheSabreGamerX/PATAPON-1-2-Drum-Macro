# PATAPON 1+2 REPLAY Drum Macro

## Description
I made this small tool for PATAPON 1+2 REPLAY to semi-automate the drumming. If you're an OG Patapon player, you know how repetitive drumming is, especially doing it in a perfect beat. Therefore, I made a Python script that's easy to use. Do take note, this does not fully automate gameplay, but simply help to avoid doing the same four-beat drumming over and over again manually.

## Controls
| Hotkey | Command |
|--------|---------|
| Y      | PATA PATA (Walk) |
| U      | PON PON (Attack) |
| I      | CHAKA CHAKA (Defend) |
| O      | Miracle (Juju) |
| H      | PON PATA (Retreat) |
| J      | PON CHAKA (Charge) |
| K      | DON DON (Jump) |
| L      | DON CHAKA (Party) |

## Notes
- You must time the first beat as usual if you want it to beat perfectly, since the drumming uses a 500ms timing. If you mess up the first beat, you will mess up the entire sequence.
- After performing the Miracle drum, you must complete the Juju sequence manually. This was not part of the automation.
- Using sequences that you haven't unlocked yet or not available in Patapon 1 (Patapon 2 Songs exclusives like DON DON and DON CHAKA) won't work.
- This is not meant to be a very sophisticated script, just a small and fun project I made to use my programming skills and use them in the games I'm playing!

## License
This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

## Requirements
- Python 3.x installed
- `keyboard` module:

```bash
pip install keyboard
