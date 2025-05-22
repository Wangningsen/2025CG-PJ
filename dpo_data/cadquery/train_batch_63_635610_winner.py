import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-29))
w1=cq.Workplane('YZ',origin=(7,0,0))
r=w0.workplane(offset=-70/2).moveTo(-22,73).cylinder(70,27).union(w1.sketch().segment((-99,3),(-18,3)).segment((-18,78)).segment((-36,78)).arc((-68,99),(-99,78)).segment((-99,76)).arc((-100,67),(-99,57)).close().assemble().finalize().extrude(43))