import cadquery as cq
w0=cq.Workplane('YZ',origin=(100,0,0))
r=w0.workplane(offset=-200/2).moveTo(70,81.5).box(40,31,200).union(w0.sketch().arc((-90,-88),(-89,-93),(-88,-97)).segment((34,-97)).segment((34,25)).segment((-90,25)).close().assemble().finalize().extrude(-7))