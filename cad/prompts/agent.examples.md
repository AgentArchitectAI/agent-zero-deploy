# user
Design a box of 100×60×40 with walls of 2 mm.
# assistant
## llama a create_model
{
 "scad_code": "
  L=100; W=60; H=40; T=2;
  difference() {
      cube([L,W,H], center=true);
      translate([0,0,T]) cube([L-2*T, W-2*T, H], center=true);
  }",
 "fmt":"stl"
}