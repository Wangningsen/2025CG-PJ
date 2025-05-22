import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-77))
r=w0.workplane(offset=56/2).moveTo(-27,80).cylinder(56,20).union(w0.sketch().push([(0,-18)]).circle(82).rect(28,86,mode='s').finalize().extrude(153))