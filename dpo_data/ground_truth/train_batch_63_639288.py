import cadquery as cq
w0=cq.Workplane('YZ',origin=(-100,0,0))
r=w0.sketch().arc((-64,41),(56,-53),(-41,64)).arc((-61,60),(-64,41)).assemble().finalize().extrude(200)