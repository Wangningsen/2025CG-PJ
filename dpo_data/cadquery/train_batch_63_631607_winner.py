import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,21,0))
w1=cq.Workplane('XY',origin=(0,0,31))
r=w0.sketch().arc((-38,-10),(-89,-70),(-28,-20)).arc((-21,-10),(-31,-9)).arc((-34,-9),(-37,-10)).segment((-37,-9)).segment((-38,-9)).close().assemble().finalize().extrude(-80).union(w0.workplane(offset=38/2).moveTo(-29.5,77).box(25,10,38)).union(w1.sketch().segment((24,-11),(73,-11)).segment((73,54)).segment((24,54)).segment((24,46)).arc((25,46),(24,45)).close().assemble().finalize().extrude(69))