import cadquery as cq
w0=cq.Workplane('YZ',origin=(100,0,0))
r=w0.sketch().segment((-33,-41),(33,41)).segment((-33,37)).close().assemble().finalize().extrude(-200)