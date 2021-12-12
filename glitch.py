pip install Pillow

from PIL import Image, ImageDraw

from google.colab import drive  
drive._mount('/content/drive')  

# open the file
with open("/content/drive/My Drive/pic.JPG") as f:
  text = f.read()
  
img = Image.open("/content/drive/My Drive/pic.JPG")
width, height = img.size
pixels = img.load()

def sort_row(row):
    min = 255*3
    min_index = 0
    #find the darkest pixel in the row
    for i in range(len(row)):
        # each pixel has an RPG value, for instance (255, 255, 255)
        temp = row[i][0] + row[i][1] + row[i][2]
        if temp < min:
            min = temp
            min_index = i
# sort the row up the brightest pixel
    sorted_row = row[:min_index]
    sorted_row.sort()
    return sorted_row + row[min_index:]
    
    // p5.js logo collage
let logo;
function preload() {
    logo = loadImage("pic.JPG");
} // end preload

function setup() {
    createCanvas(1200, 680);
    noLoop();
    background(255);
    rectMode(CENTER);
    strokeWeight(2);
    stroke(0, 0, 127);
    imageMode(CENTER);
} // end setup
    
function draw() {
    translate(width / 2, height / 2);
    (new Collage(1100, 520, 4)).render();
}  // end draw
    
function Collage(w, h, level) {
    this.w = w;
    this.h = h;
    this.level = level;
    this.render = function() {
        push();
        rotate(randomGaussian(0, 1) * (QUARTER_PI / 8 + QUARTER_PI / 32));
        let r = random(128, 256);
        let b = random(128, 256);
        let g = random(128, 256);
        fill(r, b, g, 47);
        rect(0, 0, this.w, this.h);
        if (this.level > 1) { // recursive case; create 4 Collage instances
            let coeffs = [[-1, -1], [-1, 1], [1, -1], [1, 1]];
            for (let i = 0; i <= 3; i++) {
                push();
                translate(coeffs[i][0] * this.w / 4, coeffs[i][1] * this.h / 4);
                (new Collage(this.w / 2, this.h / 2, this.level - 1)).render();
                pop();
            } // end for
        } else { // base case; display logo
            image(logo, 0, 0, 125, 57);
        }; // end else
        pop();
    } // end render
} // end Collage


new_img = Image.new('RGB',(width, height))

# to make a new image, we'll need to conver the data to a list
sorted_pixels = []
for y in range(height):
       for x in range(width):
           sorted_pixels.append(pixels[x,y])
new_img.putdata(sorted_pixels)

from google.colab.patches import cv2_imshow

draw = ImageDraw.Draw(new_img)
draw.ellipse((64,64,192,192), fill=(255,0,0))

import matplotlib.pyplot as plt
import numpy as np
plt.imshow(np.array(new_img))

