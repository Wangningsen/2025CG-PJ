import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-55))
w1=cq.Workplane('XY',origin=(0,0,-58))
r=w0.sketch().push([(-46,-8.5)]).rect(42,79).push([(54,2)]).circle(46).finalize().extrude(113).union(w1.sketch().arc((-62,28),(-99,-7),(-52,-22)).segment((-52,-28)).segment((25,-28)).segment((25,42)).segment((-62,42)).close().assemble().finalize().extrude(31))