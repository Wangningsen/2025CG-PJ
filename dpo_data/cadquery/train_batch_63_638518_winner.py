import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,2,0))
w1=cq.Workplane('XY',origin=(0,0,7))
r=w0.sketch().arc((-31,-70),(14,-34),(64,-40)).arc((-20,73),(-31,-70)).assemble().finalize().extrude(57).union(w1.sketch().segment((-100,-59),(100,-59)).segment((100,-7)).segment((-64,-7)).arc((-67,-2),(-71,-7)).segment((-100,-7)).close().assemble().push([(0,-33)]).rect(34,24,mode='s').finalize().extrude(38))