import cadquery as cq
w0=cq.Workplane('YZ',origin=(-25,0,0))
r=w0.sketch().segment((-19,-46),(-8,-53)).segment((6,-32)).segment((-2,-20)).close().assemble().finalize().extrude(-75).union(w0.sketch().push([(0,25)]).circle(28).reset().face(w0.sketch().arc((4,38),(-8,4),(13,34)).arc((12,42),(4,38)).assemble(),mode='s').finalize().extrude(125))