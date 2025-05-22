import cadquery as cq
w0=cq.Workplane('YZ',origin=(26,0,0))
w1=cq.Workplane('YZ',origin=(8,0,0))
r=w0.workplane(offset=-10/2).moveTo(46,-19).cylinder(10,26).union(w0.sketch().segment((8,-47),(82,-47)).segment((82,-36)).segment((100,-36)).segment((100,-31)).segment((82,-31)).segment((82,9)).segment((8,9)).close().assemble().finalize().extrude(6)).union(w1.workplane(offset=-40/2).moveTo(-55,2).cylinder(40,45))