import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-23,0))
w1=cq.Workplane('YZ',origin=(12,0,0))
r=w0.sketch().arc((17,25),(-32,-85),(68,-46)).arc((89,28),(17,25)).assemble().finalize().extrude(63).union(w0.sketch().push([(-46,-37)]).circle(54).reset().face(w0.sketch().segment((-90,39),(-56,39)).arc((-4,69),(-66,85)).segment((-90,85)).close().assemble()).finalize().extrude(116)).union(w1.workplane(offset=-101/2).moveTo(-26.5,7.5).box(133,103,101))