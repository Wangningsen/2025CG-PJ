import cadquery as cq
w0=cq.Workplane('YZ',origin=(82,0,0))
w1=cq.Workplane('ZX',origin=(0,85,0))
r=w0.workplane(offset=-113/2).moveTo(88,-29).cylinder(113,12).union(w0.sketch().segment((-95,15),(-26,45)).segment((-6,1)).arc((-39,93),(-86,2)).close().assemble().finalize().extrude(-79)).union(w1.sketch().segment((-93,-82),(-64,-82)).segment((-64,-74)).arc((-79,-76),(-93,-74)).close().assemble().finalize().extrude(-101))