#!/usr/bin/env python3

import subprocess
import csv
import os
import platform
import time

if platform.system() == 'Windows':
    OPENSCAD = 'C:\Program Files\OpenSCAD\openscad.exe'
elif platform.system() == 'Linux':
     OPENSCAD = 'openscad'
else:
    OPENSCAD = '/Applications/OpenSCAD.app/Contents/MacOS/OpenSCAD'

MYDIR=os.path.dirname(os.path.realpath(__file__))

def gen_samples(file=f"{MYDIR}/samples.csv"):
    os.makedirs(f"{MYDIR}/stl", exist_ok=True)
    with open(file, '+r') as f:
        data = csv.reader(f)

        for l in data:
            filename = "stl/" + "_".join(l).replace(":","_") + ".stl"
            if(os.path.isfile(filename)):
                print("Skipping:", l)
            else:
                print("Processing:", l)
                subprocess.run(
                    [OPENSCAD,
                    '-o', filename,
                    '-D', f'BRAND="{l[0]}"',
                    '-D', f'TYPE="{l[1]}"',
                    '-D', f'COLOR="{l[2]}"',
                    '-D', f'TEMP_HOTEND="{l[3]}"',
                    '-D', f'TEMP_BED="{l[4]}"',
                    f'{MYDIR}/FilamentSamples.scad',
                    ], check=True)
                time.sleep(1)


if __name__ == "__main__":
    gen_samples()
