import cadquery as cq
w0=cq.Workplane('YZ',origin=(49,0,0))
r=w0.sketch().arc((-97,-39),(95,-15),(-91,44)).arc((-90,3),(-97,-39)).assemble().finalize().extrude(-98)