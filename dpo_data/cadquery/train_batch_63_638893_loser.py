import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,14,0))
r=w0.sketch().push([(19,0)]).circle(12).push([(27,0)]).circle(2,mode='s').finalize().extrude(-114).union(w0.workplane(offset=-5/2).moveTo(0,13).box(84,58,5)).union(w0.workplane(offset=86/2).moveTo(19,0).box(40,118,86))