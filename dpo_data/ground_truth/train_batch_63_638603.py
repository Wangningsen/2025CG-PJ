import cadquery as cq
w0=cq.Workplane('YZ',origin=(97,0,0))
r=w0.sketch().segment((-81,-100),(-49,-100)).segment((-58,-94)).segment((-1,-14)).segment((-1,49)).segment((33,49)).segment((33,33)).segment((81,100)).segment((-81,100)).close().assemble().finalize().extrude(-195)