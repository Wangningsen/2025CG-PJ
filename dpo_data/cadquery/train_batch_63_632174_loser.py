import cadquery as cq
w0=cq.Workplane('YZ',origin=(42,0,0))
r=w0.sketch().push([(1,-35.5)]).rect(26,129).reset().face(w0.sketch().arc((-10,-38),(-9,-43),(-4,-46)).arc((11,-28),(-10,-38)).assemble(),mode='s').finalize().extrude(-124).union(w0.sketch().push([(0,68)]).circle(32).push([(-11,40)]).circle(2,mode='s').finalize().extrude(40))