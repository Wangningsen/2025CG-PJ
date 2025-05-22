import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,100))
r=w0.sketch().segment((-92,-5),(-81,-5)).segment((-81,-45)).segment((81,-45)).segment((81,-5)).segment((92,-5)).segment((92,5)).segment((81,5)).segment((81,45)).segment((-81,45)).segment((-81,5)).segment((-92,5)).close().assemble().finalize().extrude(-200)