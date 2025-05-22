import cadquery as cq
w0=cq.Workplane('YZ',origin=(7,0,0))
w1=cq.Workplane('XY',origin=(0,0,-29))
r=w0.sketch().segment((-99,2),(-18,2)).segment((-18,79)).segment((-37,79)).arc((-74,99),(-99,63)).close().assemble().finalize().extrude(43).union(w1.workplane(offset=-70/2).moveTo(-22,73).cylinder(70,27))