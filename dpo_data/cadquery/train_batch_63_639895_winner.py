import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-46,0))
w1=cq.Workplane('XY',origin=(0,0,-66))
r=w0.sketch().segment((-31,-100),(-27,-100)).segment((-27,-12)).arc((-28,-12),(-28,-11)).segment((-31,-11)).close().assemble().push([(-29,-55)]).circle(2,mode='s').finalize().extrude(23).union(w0.workplane(offset=44/2).moveTo(-9.5,47.5).box(85,63,44)).union(w1.sketch().push([(52,5.5)]).rect(96,81).push([(55,23)]).rect(4,20,mode='s').finalize().extrude(132))