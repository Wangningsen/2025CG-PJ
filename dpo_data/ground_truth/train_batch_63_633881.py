import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,22,0))
w1=cq.Workplane('ZX',origin=(0,37,0))
r=w0.sketch().segment((58,-45),(61,-45)).segment((61,-79)).arc((68,-69),(65,-57)).segment((77,-38)).segment((75,-37)).arc((66,27),(62,-38)).close().assemble().finalize().extrude(-59).union(w1.sketch().arc((-54,48),(-98,14),(-43,17)).segment((0,17)).segment((0,79)).segment((-54,79)).close().assemble().reset().face(w1.sketch().segment((-54,17),(-54,47)).arc((-98,14),(-43,17)).close().assemble(),mode='s').finalize().extrude(-37))