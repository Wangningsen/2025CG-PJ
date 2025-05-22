import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-27))
w1=cq.Workplane('YZ',origin=(22,0,0))
r=w0.sketch().arc((69,-94),(98,-27),(69,40)).close().assemble().finalize().extrude(-33).union(w1.workplane(offset=-120/2).cylinder(120,100))