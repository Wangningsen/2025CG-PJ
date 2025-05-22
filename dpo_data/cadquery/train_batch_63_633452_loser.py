import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,11,0))
w1=cq.Workplane('XY',origin=(0,0,-10))
r=w0.sketch().push([(-13,-21)]).circle(24).reset().face(w0.sketch().segment((26,57),(28,-13)).segment((31,-13)).segment((31,-41)).segment((100,-40)).segment((97,60)).segment((31,57)).close().assemble()).finalize().extrude(-3).union(w1.workplane(offset=-90/2).moveTo(-50,-1).cylinder(90,10))