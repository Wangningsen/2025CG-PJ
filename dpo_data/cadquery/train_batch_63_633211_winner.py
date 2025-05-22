import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,30,0))
r=w0.sketch().segment((-65,-100),(63,-100)).segment((63,23)).segment((65,23)).segment((65,42)).segment((63,42)).segment((63,100)).segment((-65,100)).close().assemble().push([(-12,-78)]).circle(9,mode='s').finalize().extrude(-60)