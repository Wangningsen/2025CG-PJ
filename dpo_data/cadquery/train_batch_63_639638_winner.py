import cadquery as cq
w0=cq.Workplane('YZ',origin=(-16,0,0))
w1=cq.Workplane('YZ',origin=(-15,0,0))
r=w0.sketch().segment((-100,26),(-69,-7)).segment((-27,33)).segment((-58,65)).close().assemble().push([(70,-35)]).circle(30).circle(25,mode='s').finalize().extrude(31).union(w1.workplane(offset=18/2).moveTo(-72,27).cylinder(18,2))