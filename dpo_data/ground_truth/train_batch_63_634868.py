import cadquery as cq
w0=cq.Workplane('YZ',origin=(100,0,0))
r=w0.sketch().segment((6,-42),(30,-42)).arc((-28,43),(37,-36)).segment((37,-8)).segment((6,-8)).close().assemble().finalize().extrude(-200)