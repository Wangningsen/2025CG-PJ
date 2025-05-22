import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-36))
r=w0.sketch().segment((46,41),(54,28)).segment((65,37)).segment((56,47)).close().assemble().finalize().extrude(21).union(w0.sketch().push([(-52,4)]).circle(48).circle(19,mode='s').push([(82,-34)]).circle(18).finalize().extrude(72))