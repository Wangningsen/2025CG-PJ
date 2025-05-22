import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,72))
r=w0.workplane(offset=-144/2).moveTo(35,0).cylinder(144,65).union(w0.sketch().segment((-100,-44),(-29,-44)).segment((-29,-55)).segment((99,-55)).segment((99,55)).segment((-29,55)).segment((-29,-36)).segment((-100,-36)).close().assemble().finalize().extrude(-45))