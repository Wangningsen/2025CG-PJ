import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-3,0))
r=w0.workplane(offset=-97/2).moveTo(0.5,0).box(21,28,97).union(w0.sketch().segment((-9,-6),(-7,-3)).segment((-5,-5)).segment((-8,-8)).arc((9,3),(-9,-6)).assemble().finalize().extrude(103))