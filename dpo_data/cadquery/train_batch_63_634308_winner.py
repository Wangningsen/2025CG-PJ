import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,100,0))
r=w0.sketch().segment((-76,-51),(-62,-51)).segment((-62,-79)).segment((62,-79)).segment((62,-51)).segment((76,-51)).segment((76,51)).segment((62,51)).segment((62,79)).segment((-62,79)).segment((-62,51)).segment((-76,51)).close().assemble().finalize().extrude(-200)