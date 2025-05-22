import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-82,0))
r=w0.workplane(offset=-18/2).moveTo(55.5,-7).box(23,174,18).union(w0.sketch().segment((-44,73),(-44,94)).arc((-45,20),(16,63)).arc((2,67),(-10,73)).close().assemble().finalize().extrude(182))