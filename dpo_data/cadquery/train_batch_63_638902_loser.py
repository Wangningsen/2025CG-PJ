import cadquery as cq
w0=cq.Workplane('YZ',origin=(4,0,0))
w1=cq.Workplane('XY',origin=(0,0,32))
r=w0.sketch().segment((-100,-32),(-94,-32)).segment((-94,-21)).arc((-97,-22),(-100,-21)).close().assemble().finalize().extrude(-25).union(w1.workplane(offset=-30/2).moveTo(0,51.5).box(44,97,30))