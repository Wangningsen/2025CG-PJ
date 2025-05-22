import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-37,0))
r=w0.sketch().push([(-76,25)]).rect(28,150).circle(2,mode='s').finalize().extrude(4).union(w0.sketch().push([(41,-51)]).circle(49).push([(87,-58)]).circle(3,mode='s').finalize().extrude(74))