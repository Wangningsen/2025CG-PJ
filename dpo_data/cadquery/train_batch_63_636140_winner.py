import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,54))
w1=cq.Workplane('XY',origin=(0,0,31))
r=w0.workplane(offset=-9/2).moveTo(28,-52).cylinder(9,48).union(w0.workplane(offset=6/2).moveTo(12,-8.5).box(78,39,6)).union(w1.sketch().segment((-76,33),(3,33)).segment((3,36)).segment((10,36)).segment((10,100)).segment((-71,100)).segment((-71,98)).segment((-76,98)).close().assemble().finalize().extrude(-91))