import cadquery as cq
w0=cq.Workplane('YZ',origin=(34,0,0))
w1=cq.Workplane('YZ',origin=(14,0,0))
r=w0.workplane(offset=-94/2).moveTo(47,74.5).box(52,51,94).union(w1.sketch().segment((-64,-100),(-29,-100)).segment((-29,16)).segment((-64,16)).segment((-64,-38)).arc((-73,-45),(-64,-53)).close().assemble().finalize().extrude(46))