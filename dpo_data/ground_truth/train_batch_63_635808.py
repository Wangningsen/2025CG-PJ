import cadquery as cq
w0=cq.Workplane('YZ',origin=(82,0,0))
w1=cq.Workplane('ZX',origin=(0,85,0))
r=w0.workplane(offset=-113/2).moveTo(88,-29).cylinder(113,12).union(w0.sketch().segment((-92,17),(-27,45)).segment((-7,1)).arc((-45,93),(-86,2)).close().assemble().finalize().extrude(-79)).union(w1.sketch().segment((-93,-82),(-64,-82)).segment((-64,-75)).segment((-67,-75)).segment((-93,-75)).close().assemble().push([(-79,-79)]).circle(3,mode='s').finalize().extrude(-101))