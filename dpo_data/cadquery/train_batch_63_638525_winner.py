import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-11,0))
w1=cq.Workplane('XY',origin=(0,0,12))
r=w0.sketch().arc((-40,49),(-45,-49),(41,-6)).segment((72,-6)).segment((72,100)).segment((-40,100)).close().assemble().finalize().extrude(-37).union(w0.workplane(offset=97/2).moveTo(8.5,78.5).box(45,29,97)).union(w1.workplane(offset=-55/2).moveTo(-55.5,-39).box(89,94,55))