import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,2,0))
r=w0.sketch().arc((-19,44),(-45,-89),(65,-9)).arc((72,90),(-19,44)).assemble().push([(17,-15)]).circle(2,mode='s').finalize().extrude(-16).union(w0.sketch().push([(-76,-80)]).circle(19).circle(2,mode='s').finalize().extrude(13))