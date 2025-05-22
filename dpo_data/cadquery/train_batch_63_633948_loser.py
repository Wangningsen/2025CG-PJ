import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-56))
w1=cq.Workplane('YZ',origin=(-25,0,0))
r=w0.workplane(offset=27/2).moveTo(9,15.5).box(106,3,27).union(w0.sketch().segment((-18,-67),(-16,-76)).arc((-6,-87),(-11,-98)).segment((-12,-100)).segment((19,-94)).segment((13,-61)).close().assemble().finalize().extrude(62)).union(w1.sketch().segment((86,50),(99,50)).arc((93,56),(86,50)).assemble().finalize().extrude(-37))