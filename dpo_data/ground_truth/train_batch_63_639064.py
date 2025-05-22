import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,21))
r=w0.workplane(offset=-121/2).cylinder(121,62).union(w0.sketch().circle(16).reset().face(w0.sketch().segment((8,2),(13,1)).segment((14,3)).segment((8,5)).close().assemble(),mode='s').finalize().extrude(79))