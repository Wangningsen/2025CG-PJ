import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,21))
r=w0.workplane(offset=-121/2).cylinder(121,62).union(w0.sketch().circle(16).push([(11,0)]).circle(4,mode='s').finalize().extrude(79))