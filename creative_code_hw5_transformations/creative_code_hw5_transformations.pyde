def setup():  
    size(400, 400)  
    rectMode(CENTER)  
  
def draw():  
    background(0)  
    from_color = color(255, 255, 0)  
    to_color = color(255, 0, 255)  
  
    # Draw a series of nested polygons  
    pushMatrix()  
    translate(width / 2, height / 2)  
    for i in range(51):  # Python uses range for loops  
        # Rotate and scale the polygons with Perlin noise  
        rotate(TWO_PI * i / 200 * noise(0.03 * frameCount))  
        scale(1 - i * 0.01 * noise(0.02 * frameCount))  
        noFill()  
        strokeWeight(3)  
        stroke(lerpColor(from_color, to_color, i / 15.0))  
        polygon(0, 0, 180, 8)  
    popMatrix()  

# custom function to draw a n-sided polygon
# https://p5js.org/examples/form-regular-polygon.html  
def polygon(x, y, radius, npoints):  
    angle = TWO_PI / npoints  
    beginShape()  
    a = 0  
    while a < TWO_PI:  
        sx = x + cos(a) * radius  
        sy = y + sin(a) * radius  
        vertex(sx, sy)  
        a += angle  
    endShape(CLOSE)  
