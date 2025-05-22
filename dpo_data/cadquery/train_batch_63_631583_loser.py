import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,28))
r=w0.workplane(offset=-56/2).moveTo(-26,-81).box(52,38,56).union(w0.sketch().push([(-43,55.5)]).rect(6,89).reset().face(w0.sketch().arc((20,0),(31,-10),(43,-1)).arc((33,33),(20,0)).assemble()).finalize().extrude(-51))