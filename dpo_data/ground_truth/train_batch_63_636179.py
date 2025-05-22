import cadquery as cq
w0=cq.Workplane('YZ',origin=(100,0,0))
r=w0.workplane(offset=-200/2).cylinder(200,35).union(w0.sketch().circle(61).reset().face(w0.sketch().segment((-55,-14),(10,-60)).segment((43,-14)).segment((-21,32)).close().assemble(),mode='s').finalize().extrude(-105))