import cadquery as cq
w0=cq.Workplane('YZ',origin=(58,0,0))
r=w0.workplane(offset=-116/2).moveTo(6,50).cylinder(116,50).union(w0.sketch().segment((-51,-100),(-38,-100)).segment((-38,-70)).arc((-34,-65),(-38,-60)).segment((-38,-30)).segment((-51,-30)).segment((-51,-60)).arc((-56,-65),(-51,-70)).close().assemble().finalize().extrude(-41))