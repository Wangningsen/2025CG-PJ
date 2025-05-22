import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,54))
w1=cq.Workplane('XY',origin=(0,0,31))
r=w0.workplane(offset=-9/2).moveTo(29,-52).cylinder(9,48).union(w0.sketch().segment((-24,-26),(2,-26)).arc((37,-29),(50,5)).segment((50,11)).segment((-24,11)).close().assemble().finalize().extrude(6)).union(w1.sketch().segment((-76,33),(6,33)).segment((6,36)).segment((10,36)).segment((10,100)).segment((-68,100)).segment((-68,98)).segment((-76,98)).close().assemble().finalize().extrude(-91))