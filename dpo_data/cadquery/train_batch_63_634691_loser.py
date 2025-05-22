import cadquery as cq
w0=cq.Workplane('YZ',origin=(34,0,0))
r=w0.workplane(offset=-122/2).cylinder(122,27).union(w0.sketch().circle(100).reset().face(w0.sketch().segment((-67,59),(-45,-77)).segment((67,-59)).segment((45,77)).close().assemble(),mode='s').finalize().extrude(54))