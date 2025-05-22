import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,8,0))
w1=cq.Workplane('XY',origin=(0,0,-40))
r=w0.workplane(offset=-108/2).moveTo(17,52).cylinder(108,38).union(w0.sketch().segment((30,-80),(37,-90)).segment((85,-55)).arc((79,-53),(73,-49)).close().assemble().finalize().extrude(92)).union(w1.sketch().arc((42,-45),(47,-21),(42,3)).close().assemble().finalize().extrude(-45))