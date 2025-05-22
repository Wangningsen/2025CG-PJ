import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,11,0))
r=w0.sketch().arc((-80,-51),(-16,-98),(8,-23)).arc((-30,-56),(-80,-51)).assemble().push([(-47,-71)]).circle(8,mode='s').finalize().extrude(-31).union(w0.sketch().push([(27,37.5)]).rect(106,125).rect(94,43,mode='s').finalize().extrude(8))