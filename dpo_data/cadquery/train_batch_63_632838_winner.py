import cadquery as cq
w0=cq.Workplane('YZ',origin=(-100,0,0))
r=w0.sketch().arc((-33,-41),(2,-2),(33,41)).segment((-33,37)).close().assemble().finalize().extrude(200)