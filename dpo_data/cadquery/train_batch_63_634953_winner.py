import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,12,0))
r=w0.sketch().arc((-80,-50),(-18,-98),(8,-23)).arc((-26,-54),(-80,-50)).assemble().push([(-47,-71)]).circle(8,mode='s').finalize().extrude(-32).union(w0.sketch().push([(27,37.5)]).rect(106,125).push([(27.5,37.5)]).rect(93,43,mode='s').finalize().extrude(7))