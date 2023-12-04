# Humanoid Modifier

Humanoid Modifier is a python script that allows to modify a humanoid urdf model in [workers folder](/workers/) for experiments with multiple humanoids for handovers with robots.

## Installation

It has developed with Tkinter for GUI and pybullet physics library.

``` $ pip install pybullet ```

## Usage

Run modifier script:
``` $ python urdf_modifier.py ```

Use the UI to modify the humanoid dimensions and the mass.

Function:
* Add new URDF model by adding a unique name.
* Update existing URDF model.
* Delete an existing URDF model.
* Visualize URDF model with pybullet physics engine.

Humanoid:
* Set the legs as non movable (fixed joints) or movable (revolute joints).

# GUI Screenshots

* Main GUI

<img src="/screenshots/main_gui.png" title="Main GUI" />

* Physics Engine GUI

<img src="/screenshots/physics_engine.png" title="Physics Engine" />

## Contributing

Please send me your changes or any improvement, bug or whatever.

## License

This is work on progress of [Felice project](https://www.felice-project.eu/) and deveoped by George Alexakis and Michalis Maniadakis.

[MIT](LICENSE)