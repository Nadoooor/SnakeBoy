# SnakeBoy — Journal Export

> [!IMPORTANT]
> Keep in mind that this is a transferred Fallout project, all the recordings are attached, and the total time is written here.
> All the journal entities made with lookout except the last entity that made with lapse. (There are about 3 hours which is already in the lookouts but also counted in the hackatime so plz remove them) It should be real 46.7h logged.

# SnakeBoy — Journal Export

- Exported at: 2026-06-26T02:30:49Z
- Project ID: 3685
- Entries: 23
- Total Hours: 46.7h

## Entry 1
- ID: 8427
- Author: Nader
- Created At: 2026-05-22T06:19:42Z

### Content

Well, I started by researching all the topics I will face while I'm working to make things easier when I'm designing.
And used Figjam for the first time, and tbh it is super great for brainstorming with it. 
Well, i search for the following topics. 
* Microcontrollers can run emulators
* Firmware I can use and edit.
* User input Buttons and joystick.
* Display and its driver.
* Sound system
* Power management system.
<br>

This all can be concluded in this FigJam diagram.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTg0MjYsInB1ciI6ImJsb2JfaWQifX0=--b48945cb8895d56cfa2fe26b61535c059a305aa9/image.png)

I will use the T-HMI-C64 firmware as it is easy to edit for the pin configurations, and if i want to like theme it to make it snake-styled.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTg0MzIsInB1ciI6ImJsb2JfaWQifX0=--bf709eb9218f3626cb50377f1b14b4dc985a0bfb/image.png)

And for the components, I made sure they are all available in my country to prevent any customs. 

Choosed the display size to be 1.8 inch as it is the best, available, and good size screen for me and its driver is  ST7735 using SPI. To prevent parallel connection, many pins.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTg0MjcsInB1ciI6ImJsb2JfaWQifX0=--2fe999ee0b48c495dfa634df824595108d7fcdfa/image.png)

Will use 12 * 12 mm buttons as they are good-sized. But for the start & select buttons, 6 * 6mm buttons are enough. Also, will use a Joystick for the movement buttons.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTg0MjgsInB1ciI6ImJsb2JfaWQifX0=--b6f2c4eb771a253fd0b45a16cab45c132831d1c9/image.png)

For the sound system, it is my first time to use that so i searched for a module called PAM8403 that can be connected to an 8 Ohm speaker and a 10Kohm potentiometer for volume adjustment. 
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTg0MjksInB1ciI6ImJsb2JfaWQifX0=--8e642e832e79795bd724dc8636e835edba33bd5f/image.png)

And for the power management system, I chose a super cool 4000mAh battery that will last for so long, along with a TP4056 charging module and a regular power switch. 
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTg0MzAsInB1ciI6ImJsb2JfaWQifX0=--a41ad9b2473d6c511de8adc58da568063874c6f3/image.png)

Can't wait to start designing it.


### Recording Links

- https://lookout.hackclub.com/api/media/efe9a1f2-fcb2-4d2a-ab17-e964ec89c8d1/video.mp4
- https://lookout.hackclub.com/api/media/110546fc-dc12-405b-a311-b2e90ff8df6c/video.mp4

## Entry 2
- ID: 8448
- Author: Nader
- Created At: 2026-05-22T09:31:15Z

### Content

Well, This session i worked on adding the components to kicad. 
Some of the components weren't in kicad by default, so i searched for them.

First, the ESP32-S3 devboard itself wasn't in Kicad. There was only the Chip itself. 
So, i used this ESP32 already in a project so i just got it from there. And yeah both the symbol and the footprint. 

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTg0NTksInB1ciI6ImJsb2JfaWQifX0=--45d4d8236790b0c8d16317be5d7f2f2c5322617b/image.png)

But the footprint wasn't the same as the ESP32-S3 dimensions that i have. It was 2mm wider. so, i edited it and add the 3D from my old project because the 3D comes with it weren't also as same as mine. 

Also, found the buttons and added them. They were so easy as i did know their dimensions when i was brainstorming.

The PAM8304 amplifier module weren't in kicad. there was also just the chip itself. so i search for it and tbh i didn't find it. so i decided to draw it myself. 
i made the footprint and will make the symbol in the next session. 

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTg0NjEsInB1ciI6ImJsb2JfaWQifX0=--c0fc1a14c1d159331dda5707cc68afc9e99ce9b7/image.png)

Also, i think it will need more improvements, but I will also see in the next session.

Finally, i searched for the joystick footprint and symbol and 3D, and i found it super easily. from SnapMagic. 

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTg0NjIsInB1ciI6ImJsb2JfaWQifX0=--567fdc9902e82a02f3dfb3b504b7feb4718823d5/image.png)
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTg0NjMsInB1ciI6ImJsb2JfaWQifX0=--155743b60a499d2320c7bd9c66f5d3a0ef096f36/image.png)
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTg0NjQsInB1ciI6ImJsb2JfaWQifX0=--c18ce1627800ab061ab85495b43aba316f38e2e4/image.png)


### Recording Links

- https://lookout.hackclub.com/api/media/1e883e16-c11e-4011-b415-8f349ba423c1/video.mp4

## Entry 3
- ID: 8644
- Author: Nader
- Created At: 2026-05-23T12:40:29Z

### Content

Well, this session I finished adding all the components' symbols, footprints, and 3D to the Kicad project. 

I started by continuing the PAM8304 symbol, i designed it to be matched with the footprint. so, when i wire everything in the schematic. it can have helper tracers in the PCB so i can trace them. 

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTg5MjcsInB1ciI6ImJsb2JfaWQifX0=--c222a07d444f72655a27b48c9e07352e27107c18/image.png)

And then i searched for the slider potentiometer and got the right size that I want, which is 4 cm long. It is smaller than the ESP32-S3 with 2 cm, so it is the perfect size. and got its footprint from SnapMagic and added it to Kicad. Of course, the potentiometer in KiCad already has its symbol. So I just used it. 

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTg5MjgsInB1ciI6ImJsb2JfaWQifX0=--8f31e9fec9f9d7eb9c4e599eae56337e6ba9812b/image.png)

After that, I search for the small connectors that i can use for the battery and the speaker and found the S2B-XH-A-1 JST XH Data Terminal Angle Male 2 Pin Connector Header 2.5mm and its male connector and found it so perfect because also i found its footprint and symbol and 3d already in kicad default libs. 
So i used it with the battery and the speaker, 

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTg5MjksInB1ciI6ImJsb2JfaWQifX0=--b2e327be8c8a86999e978d8a3d713de7654182bc/image.png)

After that, i searched for the TP4056 full module symbol and footprint to use it. but i found only the footprint. So, i made the symbol myself. 

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTg5MzAsInB1ciI6ImJsb2JfaWQifX0=--55bd9d02304f3fad88ff0a73dc1dc6781ee16922/image.png)


![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTg5MzEsInB1ciI6ImJsb2JfaWQifX0=--93112808769726d99cd35d8f1c7e62ea1b696492/image.png)

Finally, i added the power switch by searching about it in kicad and found it with the same everything so i also just used it without any modifications. 

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTg5MzIsInB1ciI6ImJsb2JfaWQifX0=--91a446c5de370703f63c07404dbace240a13e4b0/image.png)
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTg5MzMsInB1ciI6ImJsb2JfaWQifX0=--57034b3004099570a82b278de1574b61ec9d1e9a/image.png)


### Recording Links

- https://lookout.hackclub.com/api/media/d98d8877-429e-45d3-ad91-5cdf65ba0ce7/video.mp4

## Entry 4
- ID: 8970
- Author: Nader
- Created At: 2026-05-24T20:34:50Z

### Content

This will be a long one.

I started by working on the schematic and took each part separately. started with the power management.

I just connected the output charging power to the battery and the output power to the whole circuit. And connected the input to the external 5V and GND.


![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTk4MTUsInB1ciI6ImJsb2JfaWQifX0=--8c790e0321033e234b7ae7532bc9af1a8d5ce947/image.png)

After, that i worked on the controller buttons and joystick. i connected every side of the buttons at first with each other and with the ground, but i realized that i better use external pulldown resistors to save power while the device is sleeping. so i added external 10k resistors to each button. and connected them to the GND and reconnected each side of every button to the 3.3v of the esp instead of the gnd and then all the other sides of each button each to the pulldown resistor and also its pin in the ESP32. 
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTk4MjAsInB1ciI6ImJsb2JfaWQifX0=--cf46818e0fa68e56ca07319b8cffb035dc0fe8f2/image.png)

After, that i edited the symbol of the TFT screen as it has many unnecessary pins. and also edited the footprint and made it with the right dimensions. because it wasn't as same as the TFT model that i will buy. and then i connected every pin with its label. 

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTk4MjMsInB1ciI6ImJsb2JfaWQifX0=--015b6d3473d6c5723c667e2a8c7acf84646613a0/image.png)

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTk4MjQsInB1ciI6ImJsb2JfaWQifX0=--c0a145a119ec21a1393baf9a659111554a6b19f7/image.png)

After the controller, i worked on the Sound system, and thought of making it a stereo instead of a mono one. so i added a second speaker and chose another slider module that has two channels that made me tired because i didn't find a good footprint for it. So, i just downloaded a similar one and edited its dimensions  and finally i found a website called micro-ohm that sell many sliders in Egypt. So, i also got the right dimensions and model. Also, changed the symbol to be dual channel and wired everything with labels.  and yeah i slideed the pins a bit to match the 3d model of the slider pot. 

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTk4MjgsInB1ciI6ImJsb2JfaWQifX0=--5bea9126271d678777caab3d79026416156818f7/image.png)
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTk4MzAsInB1ciI6ImJsb2JfaWQifX0=--971282c2d8628e7807beecd52f3a55b1f57fa7b6/image.png)
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTk4MzMsInB1ciI6ImJsb2JfaWQifX0=--58dd186b91256c44fd0d1de39b6788e3eab4644a/image.png)

After that, i started wiring all the pins to the ESP32 but found some restrictions found on this website about the usage of some ESP32 s3 pins. [The website](https://makerspet.com/blog/esp32-s3-gpio-limitations/?srsltid=AfmBOoqyqzI1EvRlQfjRrCLPL-4SXHiGM1T6VR8RdBe_Z6hCr0fWvZQC&v=2a6a84e9e444)

So, i tried my best to connect everything without making any conflicts with the ADC2 because the wifi use them while it is active. but i found that i can use these pins as digital pins only so i will use just one with a controller button. it was kinda hard to manage that because the esp32 s3 has many limit pins so iam thinking of using a shift register but will leave that to the next session. 
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTk4MzQsInB1ciI6ImJsb2JfaWQifX0=--b4e21e6590a3fcffaf8e21db1a7652fa0c00d177/image.png)

After that, it all done. The schematic is all wired, and I will just start working on the PCB in the next session, which must be snake-style. 

And yeah, i found a really great vendor that print PCBs in Egypt with a great price and requirements called faresPCB so i contacted them and confirmed that they print vias and also got the minimum settings and searched about what they are and added them to kicad so i can design a well-made PCB that can be printed directly. 



### Recording Links

- https://lookout.hackclub.com/api/media/3cb47031-034f-46cf-b116-33193e903a98/video.mp4

## Entry 5
- ID: 9194
- Author: Nader
- Created At: 2026-05-25T20:38:43Z

### Content

Well, i tried to film my self drawing this time. 

at first i opened my figma brainstorm page and tried to think how i will make it looks like. and tbh i didn't know at first. as i want it to be a snake styled. 

So, i open pinterest to get inspired with some regular styled consoles so i can define where i will put the buttons and speakers and so on, after that i thinked how i will make it snake themed. 
so i downloaded a snake head simple image and found the it will be awsome if made it like this. 

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjAzNTEsInB1ciI6ImJsb2JfaWQifX0=--55f8c0c414270c0b127d780dbf6b618d0c9d9e27/image.png)

Well, after that i opened my camera on lookout and tried it for the first time to film myself drawing everything with the right dimensions so i can have a version in my hand that also i tried real electronics like the esp32 s2 and buttons and charging module so i can put everything in its good place. And found it to be like that 

![img-20260525-wa0078_720.jpg](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjAzNjAsInB1ciI6ImJsb2JfaWQifX0=--1c9025ebb1b9b816884d0aab2ce92965e9b9b9cf/img-20260525-wa0078_720.jpg)

After that, i switched to the laptop screen and worked on placing the PCB parts each in their perfect spot on the PCB. I put the ESP32 and the TFT display on top of each other as they will be each on a side on the PCB. 

after choosing the right spot for all of the parts. i outlined (cut-edged) the PCB to be like a handheld PCB that also can be put on a case easily. I just need to make the screw holes. 

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjAzNjEsInB1ciI6ImJsb2JfaWQifX0=--e17104fd0d618311a1e699dc2da6c4b3ea121c01/image.png)
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjAzNjIsInB1ciI6ImJsb2JfaWQifX0=--5a10de791a0dd868a9b50ece46fe1b1a6e90066b/image.png)

and that's it i finished my session :)

### Recording Links

- https://lookout.hackclub.com/api/media/7df102f2-656e-46dd-805e-6cbb3b14dd37/video.mp4
- https://lookout.hackclub.com/api/media/153b6564-c8f4-4ba0-acdc-61e99b722fe1/video.mp4
- https://lookout.hackclub.com/api/media/5a5d1d14-de44-4f68-b591-386fc00e10fa/video.mp4

## Entry 6
- ID: 9450
- Author: Nader
- Created At: 2026-05-26T19:18:37Z

### Content

Finished the PCBBBBB :)

i focused on finishing the PCB this time.

Started tracing each button with its pull-down resistor. and then i was going to trace the screen but caught that i forgot to rearrange the PIN numbers to match the real screen. 

So, i opened the footprint and edited it based on the real screen i will buy. i traced the screen to the PCB but from the Back layer, because it was on top the ESP32 but from the opposite side so i traced everything from the top layer and the screen from the back layer. 

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjA5NzcsInB1ciI6ImJsb2JfaWQifX0=--64d2a2222726fd9c0d1976f8b4008a97a59aa60a/image.png)

After tracing the screen i traced the Sound amplifier and then when i focused on tracing the Buttons to the ESP32 and  i didn't find  any place from the top layer so i traced it from the back layer like the screen  
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjA5ODAsInB1ciI6ImJsb2JfaWQifX0=--922ae778f88145424bc32d032a2799e8e812a9bc/image.png)

as well as the sound slider.

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjA5ODEsInB1ciI6ImJsb2JfaWQifX0=--0a94480e2f60a27796067ba5dabbba9a6c02dba5/image.png)

After finishing the PCB and making all the 3v7 - (GND for all the logic) as a fill solid layer and making sure all of it was traced correctly. 
I fully finished the PCB. 

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjA5ODcsInB1ciI6ImJsb2JfaWQifX0=--65e7e1dcc4b23f6318171e5cc5bd54bb5ff13ad6/image.png)

Then, i worked on the case. using Fusion. 
TBH, this freaking thing was the most awful thing i've ever used in my journey, this thing is not usable. Whenever I try to import anything, this shitty program weither crashing or takes so much time to load. 

it is so cool for rendering tho. so, I'm switching to Onshape, it is the best for me tbh. 

When finishing the case i will export and then render on this shitty program. 

When i switched to Onshape, I worked on the sketch and offset the DXF outline entity that i got from kicad that has the dimensions of the PCB. and then added the two hand pieces..

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjA5OTIsInB1ciI6ImJsb2JfaWQifX0=--51dbaa4ce52d9cbaca728270eef5913d4ec0aa80/image.png)

and that's it for this session i think i will continue the this case in the next session. 

### Recording Links

- https://lookout.hackclub.com/api/media/252e95ea-7387-4c56-bb35-17fa8622f9fa/video.mp4

## Entry 7
- ID: 9734
- Author: Nader
- Created At: 2026-05-27T19:08:46Z

### Content

uhhhhh I'm not able to lock tf in tbh, but I'm trying my best :(

Well, I tried to work this time on the 3D as much as I could. So, I worked on fixing the offsetting of the PCB outline because it was kinda broken.
And after I fixed it and it finally shaped the skitch, then I gave it an extrude for the back layer of the case to be 4 mm, as it is not very thick and not very thin at the same time, so it can last longer.  and also gave for all the outsides like the two hand-helds and the walls of the PCB inside the room, an extrude of 30 mm, so it can make the screen very close to the top case, and also the joystick and the buttons. 
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjE1OTEsInB1ciI6ImJsb2JfaWQifX0=--7fb396cfeca240f1df5b5262f533d91989cd3727/image.png)

After the extruding, i rounded the edges of the handhelds and any other sides that could be rounded, and colored it purple so the overall appearance and texture wouldn't look like a brick.

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjE1OTUsInB1ciI6ImJsb2JfaWQifX0=--663be230deea396bf3b01140cb35b776bd831a74/image.png)

But about the ESP32 and the battery on the backside. Well, I drew two Rectangles for the pin headers of the ESP32 so it can be put in or removed whenever needed from the back of the console, same thing for the battery. 

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjE1OTYsInB1ciI6ImJsb2JfaWQifX0=--0944575dad56f7fd3c2c32abd6d9fd0ca2391af0/image.png)

And also for the memory card slot i used edit in context to precisely make the square hole. The same context applies to the ESP32 pin headers and the buttery slot. 
after adding the PCB 3D to the Onshape docs of course. 

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjE1OTcsInB1ciI6ImJsb2JfaWQifX0=--6de5dac3e84f5be302c5e3bcf3332cf705d579e1/image.png)

The last thing i searched a lil about the screws i can use. i opened the hwdocs.hackclub.dev site and got from it the screw numbers that are good to use, and found them on a local merchant.
it also has many dimensions so in the next session I must work on the back and front case parts with the screw holes and dimensions. 

### Recording Links

- https://lookout.hackclub.com/api/media/2cfcff8e-f23a-46ef-8d6f-3c28e6879b83/video.mp4

## Entry 8
- ID: 9985
- Author: Nader
- Created At: 2026-05-28T19:08:23Z

### Content

Ahh forgot to say last time that i hate the 60 HOURSSS :) :) :)

Well, the Dimensions of the PCB were kinda messy, tbh i didn't make it well last time.

So, i started by editing the PCB edge cuts so I can make it with solid dimensions, so it can be easier to maintain inside the 3d and so on. 

Well, drawing the edge cuts from the KICAD itself is kinda hard. So, i drew it on Onshape and then exported it as a DXF, then I imported it into Kicad as edge cuts. 
After taking the dimensions from the PCB on Kicad, of course. 

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjI1MjgsInB1ciI6ImJsb2JfaWQifX0=--acf66ec7da5bc6e371e7ffff0080e6bcca687a5e/image.png)

After that i added the Edge cuts to the bottom case and found that i really made mess last time :(. So, basiclly i deleted it all and redid it. with really good offsets not as like as the last time. 
This time i made real good offests

- the first one is for the tolarence with just 0.3 mm
- the second on is for the Top layer mounting edges. with 8 mm
- the last one is for the out walls for the  rounding and it was 5 mm. 

And for the handhelds i made their width to be 70 mm.

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjI1MzEsInB1ciI6ImJsb2JfaWQifX0=--9cf36703f44d2ab638a439ac8acf5b22d3328f41/image.png)

I also changed the snake head style as i wanted it to has more good details with good looking so i changed it with this one by just getting a photo from the internet and using online.reaconvertor.com to convert it to DXF file that i can use on onshape. when i added it, i offsetted it so it can placed correctly. And also i extruded the snake head with 2 more millimeters so it can be prominent. 
 
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjI1MzIsInB1ciI6ImJsb2JfaWQifX0=--b7f30549223e9f80f7c050c447e9dcbb08334f4d/image.png)

After that i started with the Top case. And i made it to be 5 mm thinkness. and will make screw holes to be for a M3 screws but after i finish the full design.
Also, i used the edit in context to edit the top layer and make the holes for the buttons and the screen and the charger port and the power switch and so on. and also rounded all the holes i made to be smooth. Also i found a really super cool website for the speaker's holes and i found many designs so i just got an image from a design i loved and then converted it with the same website and used it for both the speakers.

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjI1NDEsInB1ciI6ImJsb2JfaWQifX0=--0e9be49f80fd070b5a16ba113ac3eeb4b101f129/image.png)
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjI1NDIsInB1ciI6ImJsb2JfaWQifX0=--0fce7cd95af52bd226d1a11875969d6275882885/image.png)

And yeah iam planing to change two things next session.

1. The Screens location so it can be close to the edge because of the memory card.
2. Also the Sound volume potentiometer. (I think i will prefer a round potentiometer rather then the weird slider on the back side of the SnakeBoy.)


### Recording Links

- https://lookout.hackclub.com/api/media/806dedd8-4885-4cfe-ace5-ae5bf48ec13c/video.mp4

## Entry 9
- ID: 10240
- Author: Nader
- Created At: 2026-05-29T20:08:14Z

### Content

Ahh my internet qouta ended :(

i worked a lil this time. 

i started with making a To do list with all the things i need to make.

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjMyMjYsInB1ciI6ImJsb2JfaWQifX0=--ca94d206a247f17277faa7c75bfa8db787db0c02/image.png)

after that i started by editing the PCB.

Well, i search so much to find a footprint and a 3D for the vertical shaft potentiometer instead of the slider. i found the footprint on kicad default libraries and the 3D on mouser electronics. Mouser electronics keep telling me my account is not activated but maybe it will fix by tomorrow.

So, i regularly worked on the PCB and finished moving the screen a lil more Up and changed the footprints of the potentiometer.

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjMyMzMsInB1ciI6ImJsb2JfaWQifX0=--670c80c22ad1ea21abdc657b1a9e321dc1d4b37f/image.png)

well, that is it for this session the research took most of the time. 
The next session i will need to finish the To Do list and set up the firmware and it should be finished.

### Recording Links

- https://lookout.hackclub.com/api/media/1240dec1-73ee-4ce2-a6c4-effb4673ddaa/video.mp4

## Entry 10
- ID: 10980
- Author: Nader
- Created At: 2026-06-01T19:47:44Z

### Content

FINALLY i recharged my internet quota.

I used all my streak freezes, and must journal today so here I am.

Well, i started with following what i ended up with on the last session on the to do list.

I worked on the 3D case to tidy things up and move all the Holes and so on to their new location. 

i moved the Screen square a lil up to match the PCB, and made a new hole to the potentiometer. 

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjUxMDIsInB1ciI6ImJsb2JfaWQifX0=--998fcd0836e7efbb73e2387f7bee199d587c8079/image.png)

Then, i tried to make the wall a lil more thinner so it can be more cheap and more light, Because i think 13 mm is so big. so i made it to be in total just 8 mm. 

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjUxMDcsInB1ciI6ImJsb2JfaWQifX0=--35169fdb6809d3e869da371a8bef1de625a338d3/image.png)

After that, i used the cross section tool so i can see the distance between the buttons and the top case. But the buttons was without their caps that i want to use so i imported new 12 mm buttons with their caps so i can see what is the distance with the caps. 
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjUxMTEsInB1ciI6ImJsb2JfaWQifX0=--5c98a5ad9f0c8947dd780268d72d3e19414239c3/image.png)

So, i think in the next session i will need to change the caps to designs i will make myself, or just try to left the buttons or the PCB a lil up so they can reach the top case. 

Also, iam going to remove that Hole for the SD because now i made the screen look the opposite side so the SD card will be from the inside and it will has all the Games already installed so i don't need to unplug and replug it many times. 

### Recording Links

- https://lookout.hackclub.com/api/media/e09ee28f-ecd0-4242-b7c6-13ff0c79cf6a/video.mp4

## Entry 11
- ID: 11207
- Author: Nader
- Created At: 2026-06-02T19:09:43Z

### Content

I am trying to work my best :{

I started working on the Bottom case, and I think I need to raise the PCB from the bottom structure of the case. So I made four corners. 
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjU3NzcsInB1ciI6ImJsb2JfaWQifX0=--480004f62a79d370ff0b92d456742ff86f1bc275/image.png)


At first, I made them 5 mm, but I thought it was too high because the screen was colliding with the top case, so I made it just 2 mm, but I also think now it is too low for the buttons. So I made it 4mm and made a place in the top case, but for the TFT screen board, so it can't collide with the top case. 
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjU3NzksInB1ciI6ImJsb2JfaWQifX0=--30073b4885b0213056ccebf0102047df31e10f5c/image.png)

After that, I kept thinking if there are caps also, but for the small buttons, but I didn't find any, so I modeled them myself.
I drew rectangles with the dimensions i got from the cross-section and then used the revolve tool so it can shape the small clicker that will be placed from the underside of the Top case.

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjU3ODEsInB1ciI6ImJsb2JfaWQifX0=--bdb975be0ddd062b6b73db0ca155b0f5eebb9ee6/image.png)
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjU3ODIsInB1ciI6ImJsb2JfaWQifX0=--392234d4868b46ad661207d31aa49a324dca7276/image.png)

And that's it for this session. i know it is kinda few, but I'm working on many other things else, so i just did my best :P

### Recording Links

- https://lookout.hackclub.com/api/media/5d532007-241b-4594-89ad-d1bcbe78b455/video.mp4

## Entry 12
- ID: 11386
- Author: Nader
- Created At: 2026-06-03T14:28:11Z

### Content

Made a quick session because i have a wedding to attend :)

Started with trying to download the potentiometer model again from mouser.com but it told me again i need to verify.

So, i searched my email and found the activation email again click verify.

And it worked and i got the model.

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjYzODQsInB1ciI6ImJsb2JfaWQifX0=--1b8378223dfb5fb68bb249550fdbb4407c0547f4/image.png)

After that, i added the Potentiometer to the PCB from onshape and tried to use the fastened mate to put it on the PCB. and ok it worked but. when i swtich to the main assembly. the potentiometer goes out of the PCB and it gives an error says that i can use fastened mate on two mates from the same group.

So, i just took it off from the sub-assembly of the PCB and reused the fastened mate from the main assembly itself and it worked. But i gave it a lil offset. 

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjYzODYsInB1ciI6ImJsb2JfaWQifX0=--47001836a1555e0484ffd0c410772793a6e01a36/image.png)

After that, the button caps that i found on the internet. they was kinda short and also collided with the Top case. So, i edited the caps to give them a lil more height so it can reach the other side of the Top case and it worked with these dimensions.

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjYzOTIsInB1ciI6ImJsb2JfaWQifX0=--72fc8ee0b6c0845ad5e6080dd7a12eab34ff843e/image.png)

And yeah the outter square in image is used as a revolver remover that remove the plastic that was colliding with the top case.

also found that the charging hole is kinda slided so i just moved it a lil.

And finally that what is the assembly looks like now.

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjYzOTcsInB1ciI6ImJsb2JfaWQifX0=--2ad7229a66a7e108b541d7577a750872363bbe6c/image.png)

the remaining things are the screw holes and the speakers and some more polishing. 

and yeah the battery place and how i would close the back-side



### Recording Links

- https://lookout.hackclub.com/api/media/a9af63cd-18e5-4082-be11-3ac018d3b6b6/video.mp4

## Entry 13
- ID: 11935
- Author: Nader
- Created At: 2026-06-05T20:52:23Z

### Content

THERE ARE ABOUT 15 MINUTES I FORGOT TO PAUSE AT 

Ok, i started by checking my TO DO list and found that it only remains the polishing and the screws and the backcase.

So, i started my making the back case for the battery and the ESP, I got the dimensions of the battery from the shop i will buy it from and found that it is 65*40*12 mm.

So i just drew a rectangle for it and used it as a reference. 
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6Mjc5MjEsInB1ciI6ImJsb2JfaWQifX0=--2c2a2e393fdda7d39437715657aa236ce56fd13d/image.png)

and then drew a big rec around it and the esp.

And i extruded it to like 20 mm so it can cover the esp and the battery and the i used the filet tool to make the edges smooth.

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6Mjc5MjIsInB1ciI6ImJsb2JfaWQifX0=--4d1e18bfb09d839f3de27b3bb7366836d4c12a8c/image.png)

After that i took the dimensions of the internal rectangle i made so it can be used as a holder of the back cover. And make the cover with them. and gave it two legs which can hang into two rectangle holes in the walles. and then assmbled .
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6Mjc5MjgsInB1ciI6ImJsb2JfaWQifX0=--f6d2657ef59beb95684346848a10a413f5f7348a/image.png)

After that i made a 3mm hole for the screw i will use to close this back cover and added the screw. 
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6Mjc5MjksInB1ciI6ImJsb2JfaWQifX0=--7096422f1a3d2d4c474b1ab944aebcab62d8aee6/image.png)

After that i loved how i made this for the back cover. So, iam going to use the same technique for the front cover and will give it the same legs and screw. it only uses one screw so it is kinda cool. 

i will make that next time with the polishing. i just need to make the streak for today it is 11:51 PM for me :P

### Recording Links

- https://lookout.hackclub.com/api/media/8ad2c713-bead-45f9-be63-cd2980d44bec/video.mp4

## Entry 14
- ID: 12123
- Author: Nader
- Created At: 2026-06-06T20:22:50Z

### Content

I am so close to finishing this all, yayyy.

Well, that project only remains some small finishes to be submitted. 

I started by searching for screws instead of Onshape's built-in screws because they are not good tbh. And found a real good one so i picked the biggest one and used for the Top case screws. 

and then i downloaded a bolt 3d model for M3 screws and made a place for it in the Bottom of the Bottom case because the screw was a lil bit short so i made the place for it slightly in the body. 

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6Mjg0NTgsInB1ciI6ImJsb2JfaWQifX0=--c52983c606eb0c21e92a81cfcc458b6f7d8574d9/image.png)

After making the place for it there. i used the same technique with the backcase with the same screw but i cut it a lil bit and added the bolt in its place. I loved this technique because it is easier than the copper hot bolts that sink in the plastic. i don't have this in my country in many stores so i will just use that technique. 

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6Mjg0NjgsInB1ciI6ImJsb2JfaWQifX0=--a6027dbd20bc2e1218531594dc8a8bd86d91a1d6/image.png)

After making these two screws and making them well placed. 

I finished all the importent things and now i just need to polish it a lil bit. 

So i got two drawings, a snake, and a pixel art fighter that is standing ready to fight the snake. and converted them to DXF and added them on the both handheld parts and used the extrude tool to remove 1mm inside the handheld parts, and they looks so cool for me tbh. 


![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6Mjg0NzUsInB1ciI6ImJsb2JfaWQifX0=--061b7e9e6fc57796db08e64385aef07739f348c3/image.png)

After that, i made my name on the center of the device under the screen as a credits and made a heart 'cause the text is saying "Made with LOVE, By NADER", and i extruded it up with just a  mm. 

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6Mjg0NzgsInB1ciI6ImJsb2JfaWQifX0=--8bd043183158ae54b9552a25204a91c4f99072c0/image.png)


And that's it. it looks so cool. now i just need to finish the Fallout-Zine and also edit the firmware to match all my components' pins and configurations. 



### Recording Links

- https://lookout.hackclub.com/api/media/2e8759d9-2000-441d-be3d-3532bc58adde/video.mp4

## Entry 15
- ID: 12358
- Author: Nader
- Created At: 2026-06-07T19:38:25Z

### Content

Uhhh, this firmware is kinda messy and i need to figure it out.

But the bright side is that iam learning to use "Make" and github actions for the first time.
WHYYY??

CAUSE THIS PERSON FOR SOME REASON DECIDED TO USE VERY ADVANCED TOOLS INSTEAD OF ARDUINO IDE AND PLATFORMIO.

HHHHH, Sorry about that 

Well, after i finished the whole 3D yesterday. Now, iam focusing on understanding the firmware and maintaining it. 

It is so messy for anyone to maintain, also the readme doesn't have much information (or I'm the stupid one who didn't build someone else's project before)

but i found that he said that i need to make a section in the Config.h file for my specific device. So, i made one and named it SnakeBoy and gave it all the drivers i will use. 
  
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6Mjg5OTEsInB1ciI6ImJsb2JfaWQifX0=--f09b705a28d8cf08ac399672fc983dc67cd6729c/image.png)

After that, i scrolled down and found that he was typing in each section's minion, its PIN configuration also specifies the screen dimensions, and so on. 

TBh i found that waveboard board that is already in the code was using most of my components already so i copied it and changed all the pin numbers to my pins in the schematic. 

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6Mjg5OTIsInB1ciI6ImJsb2JfaWQifX0=--ee121b47c6a67e6bdbc0008331b7239809a2a125/image.png)

After that, i tried to figure out if it is all done or i need to do something else. So, yeah i tried to build directly so it can tell me the errors. Well, i don't have unlimited internet to download many dependancies and tools. So, i knew that github actions don't use internet and just can build it for me on its server. And i already saw a build.yml file in the fork. 

So, i opened it and found that it is coool and i can use it freely. So, i search on how to run it. and then i tried to run it and wellll. it was building the whole 9 boards (Not including my board), and also a windows thing that i won't use probably, So, i opened the file to check on it. And i found that it was using all the boards. So, i deleted them and just added my board but i left the windows build cause i don't know if i will need it. 

And i relunched the build but it gave me an error saying that iam not using a FS (Filesystem) driver. So, i looked closely and found i added the board drivers in Config.h in a wrong place by mistake. so i just fixed it and it worked FOR THIS PART, 'cause it after this gave me another error looking for something called wifimanager. SOOOO

Iam gonna work on that now but i need to journal before 12AM 🤡 

### Recording Links

- https://lookout.hackclub.com/api/media/4972ce8b-6139-42d1-861a-6a832f7b4065/video.mp4

## Entry 16
- ID: 12580
- Author: Nader
- Created At: 2026-06-08T20:35:23Z

### Content

Duuh, well iam changing my firmware.

Well, tbh that firmware i was about to use is so cool and it is not a bad thing at all. But I found that it is just an emulation to the C64 device and it will be limited only to its games. 

How did i find that?

Well, i started by fixing the build in GitHub Actions and trying to see all the errors i get. So, i finished debugging and fixed all the errors (it was actually one error since yesterday, i added #else in somewhere it shouldn't be, so I just removed it.)

After the build, i found that the Windows thingy was a real full build for Windows, so i decided to try it first, and so I can understand it when i apply it on the hardware project itself. But I found it so annoying to tbh, so I searched more about why it is a console, and I found that it emulates an old device called the Commodore 64, and its games are not that good for me tbh.
this is the commodore 64:
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6Mjk1OTEsInB1ciI6ImJsb2JfaWQifX0=--7aec4d254057566e3188d4694198f395449aebef/image.png)

So, i just went to search for a big firmware that can emulate more than one platfom and more easy to use when i flash it in my snakeboy. So i found something called retro-go.

Also its building instructions are waay better. but it uses esp-idf so i went to install it too. I downloaded the installer and chose the version and let it install the esp-idf, and found an extension on vscode for it so i installed it too but it is not working.

It always gives me that it can't reach the installation of the esp-idf that i installed.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6Mjk1OTIsInB1ciI6ImJsb2JfaWQifX0=--b8a70d052c7327cc188141732719b441b98b03aa/image.png)

so, i am searching and trying to fix it right now. tried to tell it manually the paths but still i didn't work so iam gonna work on fixing that in the next session. 


### Recording Links

- https://lookout.hackclub.com/api/media/327305f2-426c-4351-bb7a-85b946e385e5/video.mp4

## Entry 17
- ID: 12853
- Author: Nader
- Created At: 2026-06-09T19:57:40Z

### Content

Well, thank god that i changed the firmware.

The retro-go is so much better. And super easy to maintain.

So, let's get it down.

So, i started reading a lot in the BUILD.md to figure out how to build and modify and so on. And this document was super cool to use. The creator made it super well. 

And yeah i fixed the VS esp-idf extension by simply choosing the version of esp-idf i have but also found that i need another version to use with retro-go, so I searched a lot on if i can just use the latest because i need to save internet qouta but nope i can't. So i just installed the desired version.

After reading in build.md and porting.md. 

I figured out many things. 

So, i started editing inside the targets in the retro-go component and just copied esp32 s3 dev kit target i found there. and changed all the pins to the pins iam using. 
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzAxODksInB1ciI6ImJsb2JfaWQifX0=--2d9150fb56f2e007c679d0e46c5ca549b01ef9ff/image.png)

And yeah i found something so much important, It is better to use the same clk, MOSI, MISO pins for all SPI devices to reduce pins usage and have enough pins.
Also i found that the ESP32 s3 doesn't have an internal DAC or I2S so, i just have two options. 
 - use external I2S component instead of the amplifier and i should change this in the PCB. 
- or trick it and use the amplifire on PWM pins but this will be less quality.

iam gonna do that in the next session but iam likely gonna change the amplifire.

after changing all the pins   and understanding the rg-inputs.
i also added the new configuration to the main configuration as like as the other configs of other boards.

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzAxOTEsInB1ciI6ImJsb2JfaWQifX0=--0b124c8cf40cdc9bbda52e6e9541f3c5e48eb243/image.png)

After that, it should be done and ready to build. 

So, i started building and found that it will build so many things for all the boards. So, i set the target to my board only (SnakeBoy). And also found that it is sometimes defaults some apps to another default board. so i changed that default board to mine.

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzAxOTIsInB1ciI6ImJsb2JfaWQifX0=--b573cc071e447ed2f08bee92d4f728cb17dc4b1c/image.png)

After that i let it build and finish building. and finally got the .img file that is ready to be flashed on an ESP32 S3. 

And that's it for the Firmware. i changed all the pins and added my board to it. 

it only remains to tesst in on the real hardware. 

And now i must work on the PCB and the Schematic to match the firmware now with the new changes and after that i should make the fallout-zine and that's it for this project. yayyy

### Recording Links

- https://lookout.hackclub.com/api/media/bc6b8dd5-7008-42e8-a1e6-5f3d7426d720/video.mp4

## Entry 18
- ID: 13086
- Author: Nader
- Created At: 2026-06-10T19:40:23Z

### Content

It is so close to finish this. 

Well, ok, gonna talk directly.  about two things i did this session.

* I did edit the PCB and add the new Sound decoder.
* I did change the 3D to match it.

Well, firstly, talking about the PCB. As the nature of Kicad, I thought it would have only the raw components not the module. 
So, i did make my own footprint & symbol for the sound decoder MAX98357, and when i went to add them to the schem and the PCB. i discovered the Big library i downloaded from ATOOMNETKICAD already had this component as a symbol and as a footprint, and also the 3D. 

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzA4MzEsInB1ciI6ImJsb2JfaWQifX0=--5de1b96146abf22c715898ac6313004e58715aa0/image.png)
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzA4MzIsInB1ciI6ImJsb2JfaWQifX0=--a0e0af21b19ef7e798dfa177221def30ce9866d4/image.png)

and TBH, i used them instead of mine because they were well-made with silkscreens for the pins. So, yeah i used them and then unrouted the components iam gonna delete like the sound volume node as it will be now integrated into the Firmware, and changed the two pins of the SD card slot to use the same pins as the screen as they are using SPI  protocol. 

After that i added the new footprint of the sound decoder and routed it to all its pins into the ESP32 and the two speakers as it will use them as mono speakers. (I will not make it stereo as it is not that important and also if i will do i will need two MAX98357 modules)

After routing that component. i did finish that PCB and i should add it to the 3D now buttttttt, I need to save my internet qouta, So i will just leave the PCB i uploaded before the latest version and will just delete the sound node hole and the potentiometer as it will not affect any other thing like the appearance or holes. So, it should be fine to leave it. 

After that, i opened the 3D and added the missing button names that I thought to add. 
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzA4MzMsInB1ciI6ImJsb2JfaWQifX0=--ab18acb5134fe2f279e82af6201dbf190586859b/image.png)

well i finished this session on that. and i must now think on a way to rainforce the PCB in the case without screws and then i can export and render and work on the zine and finally submit. 

### Recording Links

- https://lookout.hackclub.com/api/media/416bf5b9-f913-443d-b216-12eda342be63/video.mp4

## Entry 19
- ID: 13122
- Author: Nader
- Created At: 2026-06-11T01:09:04Z

### Content

Well, i made some amazing renderssss 
![Down.jpg](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzA5NzAsInB1ciI6ImJsb2JfaWQifX0=--bbb0d0ac13bce843605bd2771bf00c244f2857cd/Down.jpg)
![Purple.PNG](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzA5NzEsInB1ciI6ImJsb2JfaWQifX0=--dd74990861770ffbb5c2be8495f82201035cbed5/Purple.PNG)
![Top.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzA5NzIsInB1ciI6ImJsb2JfaWQifX0=--9e8fe970fea0a8282db47137e9d5fe668c3c4e2a/Top.png)

Well, first, before the rendering i need to talk about a quick thing.

i needed to figure out a way to reinforce the PCB in the case without screws. So the best way for me was to extrude parts from the top case to put the PCB between two toasts.

i made four courners like this at first 
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzA5NzMsInB1ciI6ImJsb2JfaWQifX0=--99adaed7385fbde30ce92acd28d1bc474f3ba2d1/image.png)

But then i thought on how i will put the top case without making it stuck. because the top case won't be put vertically, it must be put with an angle to put its legs into the holes. 

so i just made the other two corners in the middle instead of the corner 

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzA5NzQsInB1ciI6ImJsb2JfaWQifX0=--f01129e69fd96feb0c9d9a0fc3140a008a6806a4/image.png)


And also i added new two legs to the top case because it is so tall and i don''t think two legs on the edges are enough. so just in case i added these two.
. 
After i finished that, i opened fusion. But thissss  thinnnng when i imported my assembly to it. it made my whole laptop freeze unexpectedly it was so weird. tbh. and i was not able to import without crashing after that,

So, at first i gave up and kept searching about any other thing to render with and found that onshape already have that but for the preimum only not education plans.

So i just returned to fusion and found that it needs an update, So i let it update hoping it work better after that.

and yeahhhhh it worked sooooo welllll after, i think i can work on it in regular after that and design on it. 

So, i imported the assembly and tried to add some appearances but it didn't let me at first, but i found that i need to add that to the component in edit mode first i made that and also found that the black color is way better on the device. 

So i added that, and then rendered these COOOOL photos above  So, yeah i delete ever word i said about fusion.

and that's it for the FULL 3D.

I just need to start the fallout-zine designing. YAYYY

### Recording Links

- https://lookout.hackclub.com/api/media/f70500cc-b2ca-4153-a59e-66fa892bab6a/video.mp4

## Entry 20
- ID: 13333
- Author: Nader
- Created At: 2026-06-12T00:39:16Z

### Content

Worked a lil on the zine.

Well, i started working on the zine using figma and made a frame for it in the page i used for eruca-sync.
and i used the zine guide to make the frame size on it and prevent the red and blue zones.

i opened Pinterest and scrolled a lil. and i found a cool idea. 
I want the background to be a sky full of stars.

so, i asked my friend who looooves astrography to give me a good photo of the sky that has stars and it is dark blue. 

he gave me many options but i loved this one the most. 

![img-20260611-wa0065_720.jpg](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzE1ODYsInB1ciI6ImJsb2JfaWQifX0=--f1839b4aec4f1455a0699ad4a8d09bed0203ff69/img-20260611-wa0065_720.jpg)

And it is sooo coool. so iam using it and also will give him credits in my credits file. 

After that, i added the device's photos to the frame and started thinking how i will arrange that, and i found that i can put the down view of the device in the bottom side of the zine like this
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzE1ODcsInB1ciI6ImJsb2JfaWQifX0=--80567d05789e86988b947810e1cb5acbfd90af70/image.png)

dk tbh i hate any start of any design as i don't have many ideas at first, but iam gonna leave it like this for now. 

after that i found that the renders i got were not enough or not good with each other. 

So, i reopened fusion and tried to reduce the smoothness or the reflectance of the plastic and made it way better with good details. 

![duh.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzE1ODgsInB1ciI6ImJsb2JfaWQifX0=--ee7e08d35487b3da015a87d499fbfcf635ed009c/duh.png)

but iam facing a lil problem with fusion so ima fix it next sessoin. but now i also searched fontspace.com for 100% free fonts that are retro style or a lil good with the retro style
and i found this one and added it to the zine with the right top side device. 

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzE1ODksInB1ciI6ImJsb2JfaWQifX0=--dcdc1296c1da4c59b85aa689cad6d786c82380d7/image.png)

After that i added the rendered semi-photo for now on the middle of the zine to check if it will be good, and yeah it is kinda good. so i also added like a background for the middle photo and rounded its corners, but tbh the color is not that perfect so ima change it in the next session, But Overall the zine now is kinda like the layout no way a draft, but it is a good start. 
  
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzE1OTAsInB1ciI6ImJsb2JfaWQifX0=--e480ddbea7f1b900d59b8441568cac018cb94be1/image.png)


### Recording Links

- https://lookout.hackclub.com/api/media/b3d08d09-7c45-4e4a-8dd7-fca86334fbf5/video.mp4

## Entry 21
- ID: 14022
- Author: Nader
- Created At: 2026-06-14T16:45:47Z

### Content

Iam dying without internet 😭😭

But iam trying with my phone data now

Well, ok i continued working on the zine

Well, i got a very great idea this time. I can make a zine that has the colors blue and red with different levels.

And the red color can represent a planet behind the 3d render of the Device

And in the right side a rectangle that has specifications of the console and will use the same top right and middle bottom 3Ds.

I drew this all on a paper first and then started designing 


Well, i switched to canva because it will have integrated graphics and shapes.

After that i searched for a red planet and found that great one.

And also for the 3D renders, i rerendered them using fusion cloud rendering with different angles to try with.

After that, i rewrote the title with a retro effect, and with a rounding so it can be a lil bit slided down. 

And under of it, i wrote a quick sentence about the project.

After that, i added the 3D renders and chose the second image i rendered because its angle was better.

And also the middle bottom image second render was better with the colors.

So after placing them, i searched a lot for a resizable modern border box but i didn't find any.

So, i found a good bottom and top line with blue and red colors.

And i found a good box but no resizable.

So, i just cut it and connected it like a puzzle to make a rectangle for the specifications. It is not the best but can be good for now.

After that, i placed some icons and sadly my qouta ended 🥲.

So, iam gonna continue tomorrow.
![55130.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzMzMzEsInB1ciI6ImJsb2JfaWQifX0=--02d3f5971577b1f253ed6488918976d8d28de185/55130.png)
![55131.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzMzMzIsInB1ciI6ImJsb2JfaWQifX0=--e2a3a4fd512ca64c5d51f5466a5e54ce298a4d2b/55131.png)
![55132.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzMzMzMsInB1ciI6ImJsb2JfaWQifX0=--7812c0e5c44cfb0a2c38a487527ee7c31c5a9bfd/55132.png)
![55133.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzMzMzQsInB1ciI6ImJsb2JfaWQifX0=--1525a8e20c96bc4cc66f1d7d99a15b5fa19dd702/55133.png)
![55140.jpg](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzMzMzUsInB1ciI6ImJsb2JfaWQifX0=--3f585298e904f45dfac6e305f79f0618f22a58cc/55140.jpg)


### Recording Links

- https://lookout.hackclub.com/api/media/155bcf46-da6a-4c51-9f15-1b5110fde8e7/video.mp4

## Entry 22
- ID: 16235
- Author: Nader
- Created At: 2026-06-25T22:32:14Z

### Content

forgot to journal this record for  a while.

So, journaling it now.

i  was finishing the zine from the last time, it took its general shape and now i need to give it more details.

i started with the specs window (rectangle), i got some good icons and decided to put five specs. 'cause the space is enough for five. so i added the icons and wrote the specs for each icon and separated with dotted lines each between each spec and tidded up the colors to match. 

and yeah the frame with kinda awful tbh so i changed it.

and got a QR code for the repo and put it inside a red frame and made the qr itself light blue and it looks amazing. 

After that, i added the hackclub flag but the colors was kinda not matching the theme so i found a filter in Canva which made it kinda bubblely glowing, and it looks amazing.

This is the specs window right now.
![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6Mzk3NTQsInB1ciI6ImJsb2JfaWQifX0=--81050d6e78b31211cc7e57fb054bd33f7333f4eb/image.png)

after finishing this window, i worked on the description. the same color theme for the text of course has been used. but writting the "description" word in red font was kinda good so it can make the viewer know where is the description as the red color gets attention.

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6Mzk3NTYsInB1ciI6ImJsb2JfaWQifX0=--3cef73999084718b8d299e3c8f4cacffac20fab6/image.png)

after that, there was an empty space that i can use for something else, so i decided to add a steps drawings. 
i added icons for the steps how i build it (will build it). and it looks cool tbh.

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6Mzk3NTcsInB1ciI6ImJsb2JfaWQifX0=--d6349415de37d62d1a3624058325bc7137049f04/image.png)

and that's it i exported to PDF and uploaded to the repo and it looks so cool tbh as a final result.

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6Mzk3NjAsInB1ciI6ImJsb2JfaWQifX0=--2b15dc70f5de80545b1d6ea2793c6adbbda1b742/image.png)


### Recording Links

- https://lookout.hackclub.com/api/media/5767920e-b4c4-41b0-a323-aa492d8b94e9/video.mp4

## Entry 23
- ID: 16242
- Author: Nader
- Created At: 2026-06-26T02:30:07Z

### Content

Well, ok this is the last entity.

well, i didn't do much tbh. i just kept writting the readme based on my previous project's Readme So it  can match the structure. 

which consistent of: 

- Description
- Why iam making this project
- Highlight 
- Photos
- onshape docs
- how to build

this way my Readme looks so perfect and well made. 

i also added the project photos on top of the readme and centered it.

![image.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6Mzk3OTUsInB1ciI6ImJsb2JfaWQifX0=--00d0c240a961e991a93f24d6f7c1d51bcd486d0c/image.png)

after finishing the readme and i just tidded things up iin the repo so it can be readable and well organized so YOU reviewers can review it comfortably.

and that's it i finished this masterpiece. 



### Recording Links

- https://lookout.hackclub.com/api/media/9a96afa1-ed73-46aa-90f8-1fdcaf59f1fd/video.mp4
