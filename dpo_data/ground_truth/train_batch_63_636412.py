import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-3,0))
r=w0.workplane(offset=-97/2).box(20,28,97).union(w0.sketch().arc((-9,5),(8,-6),(-7,7)).arc((-8,5),(-9,5)).assemble().reset().face(w0.sketch().segment((-9,-4),(-8,-5)).segment((-7,-3)).segment((-8,-2)).close().assemble(),mode='s').finalize().extrude(103))