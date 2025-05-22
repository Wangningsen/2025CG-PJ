import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-100))
r=w0.sketch().segment((-76,-7),(-33,-69)).segment((76,7)).segment((33,69)).close().assemble().push([(-33,12)]).circle(7,mode='s').finalize().extrude(200)