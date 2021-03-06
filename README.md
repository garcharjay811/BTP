# B.Tech Project - IIT Dharwad
## Demonstrating Malware Adaptation and Designing IDSs using Advanced Learning Techniques

### Link to report
    https://www.overleaf.com/7582129669jmjvxkhcgptt

### Link to dataset
    https://drive.google.com/file/d/11A5QsrKeAQA8jW5FVq8AE2vot7M3G36v/view?usp=sharing

### Link to Google Colab
    https://colab.research.google.com/drive/1wrDDMdpq7q71QcEX1nWZbKtuib1H2m6W?usp=sharing

### Link to Stratosphere IPS for Linux
    https://github.com/stratosphereips/StratosphereLinuxIPS

### Link to Quasar RAT
    https://github.com/quasar/Quasar
Version used 1.4.0

### load_generator.py
This file loads generator weights and generates the output using this loaded generator and output is printed on terminal.

    To run: python3 load_generator.py generator.h5
generator.h5 is obtained by saving generator model weights.

### Architecture
Quasar RAT Server running on Windows 7 VM
Quasar RAT Client running on Windows 10 VM installed on Ubuntu
Stratosphere IPS installed on Ubuntu, the same machine in which Quasar RAT is installed (This is done to capture packets originating from VM)

GAN generator - Generates values and stores in a file for each run to test how good generator values are when run through IPS
                Client reads the values from the file and acts accordingly. To edit source code of Client, download the src package from github.

### Paper Followed
Bringing GAN to a Knife Fight - PDF file

### Paper referred for Image Processing Mitigation technique
Malware Classification using Image Representation - PDF file named 15111005.pdf