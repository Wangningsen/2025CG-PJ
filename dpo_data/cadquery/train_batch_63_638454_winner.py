import cadquery as cq
w0=cq.Workplane('YZ',origin=(-3,0,0))
r=w0.sketch().arc((-66,-18),(-67,-45),(-40,-46)).arc((-30,-46),(-21,-45)).arc((84,-26),(-11,25)).arc((-54,19),(-66,-18)).assemble().push([(28.5,-16.5)]).rect(35,33,mode='s').finalize().extrude(-97).union(w0.workplane(offset=103/2).moveTo(-81,24.5).box(8,97,103))