import cadquery as cq
w0=cq.Workplane('YZ',origin=(32,0,0))
r=w0.sketch().arc((21,98),(-89,-44),(99,-21)).arc((-15,-5),(21,98)).assemble().finalize().extrude(-64)