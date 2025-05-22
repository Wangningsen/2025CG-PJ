import cadquery as cq
w0=cq.Workplane('YZ',origin=(-18,0,0))
r=w0.sketch().arc((-45,-18),(-98,-63),(-29,-68)).arc((7,-30),(-45,-18)).assemble().push([(-62,-52)]).rect(16,18,mode='s').finalize().extrude(-73).union(w0.workplane(offset=108/2).moveTo(41.5,50).box(117,78,108))