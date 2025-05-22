import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-3,0))
r=w0.sketch().segment((-100,-79),(-68,-79)).segment((-68,-93)).segment((100,-93)).segment((100,-45)).segment((-9,-45)).segment((-9,93)).segment((-100,93)).close().assemble().finalize().extrude(7)