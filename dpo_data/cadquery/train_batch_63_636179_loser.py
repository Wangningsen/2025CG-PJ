import cadquery as cq
w0=cq.Workplane('YZ',origin=(100,0,0))
r=w0.workplane(offset=-200/2).cylinder(200,35).union(w0.sketch().circle(61).reset().face(w0.sketch().segment((-53,-7),(5,-57)).segment((53,7)).segment((-5,57)).close().assemble(),mode='s').finalize().extrude(-105))