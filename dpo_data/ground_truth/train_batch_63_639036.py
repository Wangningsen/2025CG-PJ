import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-48))
w1=cq.Workplane('XY',origin=(0,0,-35))
r=w0.sketch().push([(-44,-52)]).circle(48).reset().face(w0.sketch().arc((30,76),(45,17),(90,58)).arc((70,99),(30,76)).assemble()).finalize().extrude(100).union(w0.sketch().segment((25,60),(85,60)).arc((55,83),(25,60)).assemble().finalize().extrude(118)).union(w1.sketch().segment((13,9),(67,9)).segment((67,36)).segment((64,36)).arc((55,69),(47,36)).segment((13,36)).close().assemble().finalize().extrude(-34))