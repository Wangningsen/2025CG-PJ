import cadquery as cq
w0=cq.Workplane('YZ',origin=(-17,0,0))
w1=cq.Workplane('YZ',origin=(-18,0,0))
r=w0.sketch().arc((-44,-18),(-98,-63),(-28,-68)).arc((7,-29),(-44,-18)).assemble().push([(-62,-52)]).rect(16,18,mode='s').finalize().extrude(-73).union(w0.workplane(offset=107/2).moveTo(41.5,50).box(117,78,107)).union(w1.workplane(offset=33/2).moveTo(-14.5,59).box(5,6,33))