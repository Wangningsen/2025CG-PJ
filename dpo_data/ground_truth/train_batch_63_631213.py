import cadquery as cq
w0=cq.Workplane('YZ',origin=(-99,0,0))
r=w0.sketch().segment((-100,-39),(-80,-72)).segment((100,39)).segment((80,72)).close().assemble().finalize().extrude(199)