#!/usr/bin/env python3

import subprocess
import argparse

# parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("scale", type=float)
args = ap.parse_args()

#run algo
#cartoon-texture images
subprocess.run(['cartoonTexture', 'input_0.png', str(args.scale), 
                    'cartoon.png', 'texture.png'])
