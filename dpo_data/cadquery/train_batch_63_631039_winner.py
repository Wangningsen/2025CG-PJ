import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-6))
w1=cq.Workplane('XY',origin=(0,0,-39))
r=w0.workplane(offset=-94/2).moveTo(-80,45).cylinder(94,15).union(w0.sketch().segment((-17,-62),(64,-62)).segment((64,-42)).arc((86,38),(1,43)).segment((-17,43)).close().assemble().push([(41,8)]).circle(10,mode='s').finalize().extrude(-22)).union(w0.sketch().arc((12,-27),(23,-30),(35,-27)).close().assemble().reset().face(w0.sketch().segment((12,8),(35,8)).arc((23,12),(12,8)).assemble()).finalize().extrude(106)).union(w1.workplane(offset=7/2).moveTo(28.5,-9).box(13,20,7))