# Pi In the Sky
## Equations
Everyone needs some equations to define various bits 'n pieces. Here are ours:

(number of balloons) = 81.7 * (mass in kilograms)

(ft<sup>3</sup> of helium) = 33 * (mass in kilograms)
## The Build
NEEDS CONTENT
## The Stuff Inside
The house's contents are:
* One (1) Raspberry Pi Zero
* One (1) MPL3115A2 Plus altimeter
* One (1) LSM303DLHC accelerometer
* One (1) Tower Pro SG92R Micro servo
* One (1) 400 Tie Point Solderless Breadboard
* One (1) PowerBost 500 Charger
* One (1) 3.7v lithium ion battery
* One (1) USB OTG MicroB cable
* One (1) MicroSD card
* ~Fifty centimetres (50cm) wire

![text](/Fritzing-Pic.PNG)
The wiring is picured above. The cyan rectangles represent the altimeter and accelerometer.

## The Code
link to code?

## The Schedule
### January
_Day 1 through Day 12_

__January 9 - Day 1__

We began the project early. Because of this, we deviated slightly from the schedule by planning out the size (and ground floor shape) of the house.

__January 10 - Day 2__

We mostly finished the floor plan and decided against including a camera. We also began to mass the necessary components.

__January 13 - Day 3__

We finished the ground floor and began to work on the top floor.

__January 14 - Day 4__

We began to create the actual building (walls, etc.).

__January 16 - Day 5__

We finished the ground floor and began the second floor.

__January 17 - Day 6__

We had a half day, so we weren't able to make much progress on the project.

__January 22 - Day 7__

We finished the second floor and chimney, and began making the roof.

__January 23 - Day 8__

We continued making the roof and began working on the walls for the second story.

__January 24 - Day 9__

We made half of the roof and are a mere five or so parts away from completion of the house.

__January 27 - Day 10__

We finished creating the acual architecture of the house, and have moved on to the code.

__January 28 - Day 11__

We figured out how to control a servo with the Pi, and we began to take the steps necessary to save inputs (the accelerometer data) to a .txt file.

__January 30 - Day 12__

Aidan discovered how to read and write a .txt file, as well as how to save it. He began making test code that would simply write accelerometer data to a .txt file.

### Febuary
_Day 13 through Day --_

__Febuary 3 - Day 13__

Aidan almost finished the test .txt writer.

__Febuary 4 - Day 14__

We finished the writer, and began to learn how to use the altimeter.

__Febuary 6 - Day 15__

We transcribed altimeter code we found on the internet and discovered that we need a special library.

__Febuary 7 - Day 16__

We completed the altimeter code and got it in working order. We have a few goals for the rest of the code: decide the autosave interval; decide the altitude when the project descends; set the altitude to zero on startup; and record the altitude, accelerometer data, and time to a .txt file.

__Febuary 10 - Day 17__

We did all the aformentioned tasks. Great! The one thing we didn't do was connect the servo to the system so that it moves at a specified altitude.

__Febuary 11 - Day 18__

We connected the servo and finished the code! We also commented it and re-arranged the wiring to save space and about 50g.

__Febuary 13 - Day 19__

We spent the day debugging the code, because when the code is finished, it is never actually finished.

__Febuary 14 - Day 20__

Aidan worked on the Fritzing diagram, and Cade continued debugging.
