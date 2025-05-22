import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-8))
r=w0.sketch().arc((-56,3),(-25,-99),(-23,7)).arc((-50,100),(-56,3)).assemble().reset().face(w0.sketch().segment((-70,-83),(4,-83)).segment((4,-16)).segment((-20,-16)).arc((-25,-15),(-31,-16)).segment((-70,-16)).close().assemble(),mode='s').finalize().extrude(-21).union(w0.workplane(offset=37/2).moveTo(56,-15).cylinder(37,37))