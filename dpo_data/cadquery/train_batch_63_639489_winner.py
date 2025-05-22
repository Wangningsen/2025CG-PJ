import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,13))
w1=cq.Workplane('XY',origin=(0,0,6))
r=w0.sketch().segment((-40,-90),(-4,-100)).segment((1,-82)).arc((5,-74),(6,-65)).segment((14,-32)).segment((-23,-22)).segment((-30,-54)).arc((-33,-61),(-33,-69)).close().assemble().finalize().extrude(2).union(w1.sketch().arc((-50,42),(40,21),(2,100)).segment((2,42)).close().assemble().finalize().extrude(-21))