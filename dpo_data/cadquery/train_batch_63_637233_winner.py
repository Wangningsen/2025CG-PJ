import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-61))
r=w0.workplane(offset=-39/2).moveTo(0,-2).cylinder(39,35).union(w0.sketch().segment((-41,31),(-11,0)).segment((-11,-5)).segment((-8,-5)).segment((28,-43)).segment((41,-31)).segment((-28,43)).close().assemble().finalize().extrude(161))