import cadquery as cq
w0=cq.Workplane('YZ',origin=(-100,0,0))
r=w0.sketch().segment((-60,-1),(44,-41)).segment((60,1)).segment((-44,41)).close().assemble().finalize().extrude(200)