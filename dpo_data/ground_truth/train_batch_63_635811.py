import cadquery as cq
w0=cq.Workplane('YZ',origin=(-29,0,0))
r=w0.workplane(offset=8/2).moveTo(27,34).box(146,44,8).union(w0.sketch().segment((-44,-43),(-44,-38)).segment((-41,-38)).arc((-96,-9),(-44,-43)).assemble().finalize().extrude(58))