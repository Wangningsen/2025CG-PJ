import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-23))
r=w0.workplane(offset=-77/2).cylinder(77,34).union(w0.workplane(offset=79/2).moveTo(0,-34.5).box(44,17,79)).union(w0.sketch().segment((-62,-10),(-44,-44)).segment((14,-15)).segment((34,-15)).segment((34,-4)).segment((62,10)).segment((44,44)).segment((-14,15)).segment((-34,15)).segment((-34,4)).close().assemble().finalize().extrude(123))