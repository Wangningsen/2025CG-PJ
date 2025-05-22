import cadquery as cq
w0=cq.Workplane('YZ',origin=(82,0,0))
w1=cq.Workplane('ZX',origin=(0,-16,0))
r=w0.workplane(offset=-113/2).moveTo(88,-29).cylinder(113,12).union(w0.sketch().segment((-95,14),(-27,45)).segment((-7,1)).arc((-39,93),(-86,3)).close().assemble().finalize().extrude(-79)).union(w1.sketch().segment((-93,-82),(-78,-82)).segment((-78,-80)).segment((-75,-80)).segment((-75,-82)).segment((-64,-82)).segment((-64,-75)).segment((-93,-75)).close().assemble().finalize().extrude(101))