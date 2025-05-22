import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-49,0))
w1=cq.Workplane('ZX',origin=(0,-57,0))
r=w0.sketch().segment((-100,-98),(13,-98)).segment((13,-9)).arc((69,75),(12,-8)).segment((-100,-8)).close().assemble().finalize().extrude(105).union(w1.workplane(offset=66/2).moveTo(-57,89).box(8,18,66))