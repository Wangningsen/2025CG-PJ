import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,100))
w1=cq.Workplane('YZ',origin=(14,0,0))
r=w0.workplane(offset=-51/2).moveTo(-13,47).box(94,52,51).union(w1.sketch().segment((-64,-100),(-29,-100)).segment((-29,16)).segment((-64,16)).segment((-64,-38)).arc((-73,-46),(-64,-54)).close().assemble().finalize().extrude(46))