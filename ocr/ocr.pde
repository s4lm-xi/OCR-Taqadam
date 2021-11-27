void setup(){
  size(800, 600);
  background(102);
}



void draw(){
  
  stroke(255);
  strokeWeight(10);
  if (mousePressed == true) {
    line(mouseX, mouseY, pmouseX, pmouseY);
  }

}
