import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,30,0))
r=w0.sketch().segment((-65,-100),(63,-100)).segment((63,23)).arc((65,33),(63,45)).segment((63,100)).segment((-65,100)).close().assemble().push([(-13,-79)]).circle(9,mode='s').finalize().extrude(-60)