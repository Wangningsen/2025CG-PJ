import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,54))
w1=cq.Workplane('XY',origin=(0,0,54))
r=w0.workplane(offset=31/2).cylinder(31,4).union(w0.sketch().segment((-61,-18),(-28,-18)).arc((0,-33),(28,-18)).segment((61,-18)).segment((61,18)).segment((28,18)).arc((0,33),(-28,18)).segment((-61,18)).close().assemble().finalize().extrude(31)).union(w0.workplane(offset=32/2).box(122,142,32)).union(w1.sketch().rect(200,84).push([(-82,-31)]).circle(3,mode='s').push([(44,29)]).circle(11,mode='s').finalize().extrude(-139))