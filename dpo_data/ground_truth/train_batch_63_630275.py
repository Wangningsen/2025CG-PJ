import cadquery as cq
w0=cq.Workplane('YZ',origin=(-2,0,0))
r=w0.sketch().arc((7,73),(33,65),(8,76)).arc((9,74),(7,73)).assemble().push([(19.5,62)]).rect(7,6,mode='s').finalize().extrude(-98).union(w0.workplane(offset=102/2).moveTo(0,-34).box(70,98,102))