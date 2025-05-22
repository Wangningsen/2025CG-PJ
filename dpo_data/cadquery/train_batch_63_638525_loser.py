import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-11,0))
w1=cq.Workplane('YZ',origin=(-11,0,0))
r=w0.sketch().arc((-40,49),(-46,-50),(42,-6)).segment((72,-6)).segment((72,100)).segment((-40,100)).close().assemble().finalize().extrude(-37).union(w0.workplane(offset=97/2).moveTo(8.5,78.5).box(45,29,97)).union(w1.workplane(offset=-89/2).moveTo(-39,-15.5).box(94,55,89))