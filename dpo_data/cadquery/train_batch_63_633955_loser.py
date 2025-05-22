import cadquery as cq
w0=cq.Workplane('YZ',origin=(25,0,0))
w1=cq.Workplane('YZ',origin=(25,0,0))
r=w0.sketch().arc((-57,-15),(-41,-64),(4,-91)).segment((11,-100)).segment((22,-93)).segment((22,-92)).arc((90,-14),(29,56)).arc((-68,86),(-57,-15)).assemble().finalize().extrude(-50).union(w1.workplane(offset=-14/2).moveTo(-25,38).cylinder(14,28))