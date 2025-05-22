import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-82))
r=w0.sketch().arc((-35,5),(-26,-98),(32,-10)).arc((22,98),(-35,5)).assemble().push([(-11.5,-45)]).rect(17,52,mode='s').finalize().extrude(84).union(w0.sketch().push([(-11.5,-45)]).rect(9,44).push([(-11,-45)]).circle(3,mode='s').finalize().extrude(164))