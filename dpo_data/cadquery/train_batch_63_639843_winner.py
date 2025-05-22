import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,15))
r=w0.workplane(offset=-61/2).moveTo(28,0).cylinder(61,72).union(w0.sketch().segment((-100,-23),(-25,-42)).arc((-17,-48),(-8,-52)).segment((43,-65)).segment((69,23)).segment((14,40)).arc((6,43),(-3,45)).segment((-72,66)).close().assemble().finalize().extrude(30))