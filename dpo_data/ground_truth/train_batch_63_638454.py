import cadquery as cq
w0=cq.Workplane('YZ',origin=(-3,0,0))
r=w0.sketch().arc((-66,-18),(-66,-46),(-37,-45)).arc((-29,-46),(-21,-45)).arc((84,-24),(-12,25)).arc((-53,21),(-66,-18)).assemble().push([(28.5,-16)]).rect(35,34,mode='s').finalize().extrude(-97).union(w0.workplane(offset=103/2).moveTo(-81,24.5).box(8,97,103))