import cadquery as cq
w0=cq.Workplane('YZ',origin=(-26,0,0))
w1=cq.Workplane('YZ',origin=(-26,0,0))
r=w0.sketch().segment((-77,-2),(-71,-2)).segment((-71,2)).segment((-24,2)).arc((-12,28),(16,15)).arc((24,53),(3,86)).segment((3,92)).segment((-4,92)).arc((-34,100),(-65,92)).segment((-71,92)).segment((-71,89)).arc((-94,44),(-77,-2)).assemble().finalize().extrude(-18).union(w0.workplane(offset=69/2).moveTo(39,-45).cylinder(69,55)).union(w1.sketch().arc((2,-4),(-1,-7),(3,-6)).arc((1,-5),(2,-4)).assemble().finalize().extrude(70))