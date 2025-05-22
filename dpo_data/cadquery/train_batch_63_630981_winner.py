import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-1))
w1=cq.Workplane('XY',origin=(0,0,-19))
r=w0.workplane(offset=-59/2).moveTo(31,-10).cylinder(59,46).union(w0.sketch().push([(-33,56)]).circle(44).push([(41,-70)]).circle(30).push([(26,-52)]).circle(3,mode='s').finalize().extrude(93)).union(w1.sketch().push([(31,-10)]).circle(31).circle(27,mode='s').finalize().extrude(-73))