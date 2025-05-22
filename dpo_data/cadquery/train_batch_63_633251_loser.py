import cadquery as cq
w0=cq.Workplane('YZ',origin=(-17,0,0))
r=w0.sketch().arc((-45,-17),(-98,-63),(-28,-65)).arc((6,-28),(-45,-17)).assemble().push([(-62,-52.5)]).rect(16,17,mode='s').finalize().extrude(-73).union(w0.workplane(offset=107/2).moveTo(41.5,50).box(117,78,107))