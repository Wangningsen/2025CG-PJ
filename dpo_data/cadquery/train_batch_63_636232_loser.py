import cadquery as cq
w0=cq.Workplane('YZ',origin=(-32,0,0))
r=w0.sketch().arc((20,98),(-86,-49),(99,-22)).arc((-14,-7),(20,98)).assemble().finalize().extrude(64)