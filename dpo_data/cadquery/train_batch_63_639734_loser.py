import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,80))
r=w0.sketch().segment((-80,-97),(-77,-100)).segment((-56,-72)).segment((-59,-71)).close().assemble().push([(44,61.5)]).rect(72,77).finalize().extrude(-161)