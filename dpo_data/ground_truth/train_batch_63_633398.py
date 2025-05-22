import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-82))
r=w0.sketch().arc((-35,4),(-23,-99),(31,-11)).arc((20,99),(-35,4)).assemble().push([(-11.5,-45.5)]).rect(17,51,mode='s').finalize().extrude(84).union(w0.sketch().push([(-11.5,-45.5)]).rect(9,43).push([(-11,-45)]).circle(4,mode='s').finalize().extrude(164))