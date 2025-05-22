import cadquery as cq
w0=cq.Workplane('YZ',origin=(-59,0,0))
w1=cq.Workplane('XY',origin=(0,0,-14))
r=w0.sketch().arc((-31,45),(-88,-33),(-9,21)).arc((-21,37),(-31,45)).assemble().finalize().extrude(79).union(w1.sketch().push([(0,77.5)]).rect(140,45).reset().face(w1.sketch().segment((-9,59),(-3,59)).segment((-3,53)).segment((3,53)).segment((3,59)).segment((9,59)).segment((9,98)).segment((3,98)).segment((3,100)).segment((-3,100)).segment((-3,98)).segment((-9,98)).close().assemble(),mode='s').push([(34,58)]).circle(1,mode='s').finalize().extrude(29))