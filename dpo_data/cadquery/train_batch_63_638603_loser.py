import cadquery as cq
w0=cq.Workplane('YZ',origin=(-97,0,0))
r=w0.sketch().segment((-81,-100),(-49,-100)).arc((-47,-78),(-36,-62)).segment((-35,-60)).segment((-34,-61)).arc((-19,-39),(-1,-19)).segment((-1,49)).segment((33,49)).segment((33,33)).arc((61,72),(81,100)).segment((-81,100)).close().assemble().finalize().extrude(194)