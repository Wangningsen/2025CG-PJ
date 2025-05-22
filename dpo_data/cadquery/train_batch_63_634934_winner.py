import cadquery as cq
w0=cq.Workplane('YZ',origin=(100,0,0))
r=w0.sketch().segment((-5,-10),(5,-24)).segment((14,-14)).arc((4,-12),(-5,-10)).assemble().finalize().extrude(-200).union(w0.workplane(offset=-71/2).cylinder(71,24))