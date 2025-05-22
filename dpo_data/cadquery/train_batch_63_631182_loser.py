import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,30))
w1=cq.Workplane('ZX',origin=(0,-15,0))
r=w0.workplane(offset=-118/2).moveTo(75,66).cylinder(118,25).union(w0.sketch().arc((-58,-47),(27,-77),(-1,9)).arc((-84,40),(-58,-47)).assemble().finalize().extrude(58)).union(w1.workplane(offset=51/2).moveTo(26,-51).cylinder(51,14))