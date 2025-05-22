import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,2,0))
w1=cq.Workplane('XY',origin=(0,0,45))
r=w0.sketch().arc((-30,-70),(12,-35),(65,-40)).arc((-21,73),(-30,-70)).assemble().finalize().extrude(57).union(w1.sketch().segment((-100,-59),(100,-59)).segment((100,-7)).segment((-58,-7)).arc((-68,-4),(-78,-7)).segment((-100,-7)).close().assemble().push([(0,-50)]).rect(34,10,mode='s').push([(0,-17)]).rect(34,10,mode='s').finalize().extrude(-38))