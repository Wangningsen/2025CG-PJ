import cadquery as cq
w0=cq.Workplane('YZ',origin=(-32,0,0))
r=w0.sketch().arc((21,98),(-83,-55),(99,-21)).arc((-13,-9),(21,98)).assemble().finalize().extrude(64)