# HANAGOTCHI
<img width="567" height="807" alt="image" src="https://github.com/user-attachments/assets/cd4648ab-0474-4b21-a38f-8ce40088ae58" />
  
A small "tamagotchi", shaped like a flower. It has three interactive buttons and an OLED screen, and can play many different files-- coded in micropython. This isn't a generic "pet" tamagotchi-- you're guarding a dangerous invisible criminal-- try not to let them get out!!  

## ***Inspiration***
As a constant fiction writer, I've always wanted to create my own special dialogue-based game. This gave me the perfect chance to do so, while including extrenally aeshtetic pleasures as well.

## ***Full Instructions~***

**getting the pcb**
1. go to https://jlcpcb.com/. click "get instant quote".
2. download the gerber zip file from the pcb folder and upload it.
3. you can change the color of the PCB if you'd like, but keep all the other settings the same.
4. order your PCB by following the steps on the website.

**getting the parts**
1. To find all the suitable parts needed for this pcb, open the BOM file. This lists all the necessary parts needed for the PCB-- you'll see several links leading to product pages.

**printing the case**
1. download the STL files, or go open this onshape link: [https://cad.onshape.com/documents/30ca1b2b31257d2650154877/w/6a6ce5b2935f39e9888c6e90/e/9cf32ad964649424d66e1c2f?renderMode=0&uiState=6a1fb2345d12723005a9a689](https://cad.onshape.com/documents/cbb68b9589daf277c9578781/w/eef88f9737002ddb59d7612d/e/e6992a34dc4435c059d9da9e?renderMode=0&uiState=6a20adc240c23c91ee920c5a).
2. follow the directions on your own 3D printer's manufacturer's website/app to upload the STL files in and print them. support for the prints are not neeeded, as long as you have the models sitting on the correct side.

**soldering and putting everything together**
1. solder the pieces together in their designated spots. You can use the .step file to see how it should look like in the end (the battery cell is optional). 
2. After you're done soldering it, plug the ESP32 into your device using a USB-C.
3. Import micropython onto your ESP32 by uploading the ESP32_GENERIC_C3-20260406-v1.28.0.bin into the adafruit webserial bootloader (https://adafruit.github.io/Adafruit_WebSerial_ESPTool/)(to start this, click the "connect" button on the upper right corner. no offset is needed.).
4. upload the programs into the ESP32 using your coding development environment (ex; Thonny.) whenever you plug in the device, it should immeadiately start playing the intro (main) file!!



## ***GALLERY***
<details>
  <summary>3D model, PCB design, schematic, etc</summary>
<img width="877" height="745" alt="image" src="https://github.com/user-attachments/assets/cf3626e4-649e-4582-aaf3-1dd5cbdc16d7" />
<img width="741" height="721" alt="image" src="https://github.com/user-attachments/assets/a1da38c4-27fb-4b74-bf10-579afb266f47" />
<img width="912" height="855" alt="image" src="https://github.com/user-attachments/assets/e04995ed-58f1-4e2f-9212-aef25ab4955a" />
<img width="936" height="875" alt="image" src="https://github.com/user-attachments/assets/5edc34f3-2803-4226-8fe9-bbad878d5a77" />
<img width="1428" height="933" alt="image" src="https://github.com/user-attachments/assets/6707f788-2f0c-439e-9d9f-83f6fe4b7fe6" />
<img width="716" height="661" alt="image" src="https://github.com/user-attachments/assets/f162d73c-6993-4076-931b-3526719d9ceb" />
<img width="362" height="395" alt="image" src="https://github.com/user-attachments/assets/a9893654-7c57-4536-8cc1-ac792ca504f6" />
<img width="454" height="591" alt="image" src="https://github.com/user-attachments/assets/02c8e094-631d-4de2-9b57-8ef4df80c2a1" />

</details>

## ***Credits~***
This project used:
- [KiCAD](https://www.kicad.org/) (for PCB design)
- [Onshape](https://www.onshape.com/en/platform) (for case design)
- [@TaniWanKenobi's Tamagotchi Guided Tutorial](https://fallout.hackclub.com/docs/guided-projects/tamagotchi) (for the base schematic layout) 
