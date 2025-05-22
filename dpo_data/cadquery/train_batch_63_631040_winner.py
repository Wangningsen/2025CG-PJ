import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,65))
r=w0.sketch().push([(36,78)]).circle(22).reset().face(w0.sketch().segment((15,79),(26,78)).segment((26,84)).segment((16,85)).close().assemble(),mode='s').finalize().extrude(-130).union(w0.workplane(offset=-114/2).moveTo(0,-12).cylinder(114,88))