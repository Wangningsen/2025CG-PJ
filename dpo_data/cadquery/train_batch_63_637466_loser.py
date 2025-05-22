import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,72))
r=w0.workplane(offset=-144/2).moveTo(-55,20).cylinder(144,45).union(w0.sketch().segment((79,-38),(97,-65)).segment((100,-63)).segment((81,-38)).close().assemble().finalize().extrude(-7))