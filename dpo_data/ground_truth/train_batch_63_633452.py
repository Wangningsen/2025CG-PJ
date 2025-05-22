import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,8,0))
w1=cq.Workplane('XY',origin=(0,0,-10))
r=w0.sketch().push([(-13,-21)]).circle(24).reset().face(w0.sketch().segment((26,57),(29,-42)).segment((100,-40)).segment((97,60)).close().assemble()).finalize().extrude(3).union(w1.workplane(offset=-90/2).moveTo(-50,-1).cylinder(90,10))