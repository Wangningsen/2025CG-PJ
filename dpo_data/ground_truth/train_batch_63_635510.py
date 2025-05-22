import cadquery as cq
w0=cq.Workplane('YZ',origin=(-93,0,0))
r=w0.sketch().arc((-100,-72),(-97,-73),(-98,-76)).arc((-79,-66),(-100,-72)).assemble().finalize().extrude(68).union(w0.workplane(offset=187/2).moveTo(71,67.5).box(58,25,187))