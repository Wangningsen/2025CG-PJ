import cadquery as cq
w0=cq.Workplane('YZ',origin=(-75,0,0))
r=w0.sketch().arc((-49,-93),(0,-82),(49,-94)).arc((0,94),(-49,-93)).assemble().finalize().extrude(150)