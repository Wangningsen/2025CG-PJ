import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-32,0))
w1=cq.Workplane('XY',origin=(0,0,-11))
r=w0.sketch().segment((-62,-42),(-25,-100)).segment((-10,-90)).segment((-10,-97)).segment((10,-97)).segment((10,-78)).segment((62,-46)).segment((25,12)).segment((10,2)).segment((10,8)).segment((-10,8)).segment((-10,-11)).close().assemble().finalize().extrude(-31).union(w1.sketch().arc((1,-14),(97,-16),(27,53)).arc((-32,38),(1,-14)).assemble().reset().face(w1.sketch().arc((3,-7),(10,16),(23,34)).arc((-4,27),(3,-7)).assemble(),mode='s').finalize().extrude(35))