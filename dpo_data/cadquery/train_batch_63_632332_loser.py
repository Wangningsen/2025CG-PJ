import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-95))
r=w0.workplane(offset=-5/2).moveTo(-30,-51).cylinder(5,40).union(w0.sketch().segment((-47,-18),(-43,-18)).segment((-47,-15)).close().assemble().finalize().extrude(139)).union(w0.sketch().segment((-47,-42),(73,-42)).segment((73,91)).segment((46,91)).arc((19,78),(-6,91)).segment((-47,91)).close().assemble().finalize().extrude(195))