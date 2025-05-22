import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,100,0))
r=w0.workplane(offset=-200/2).moveTo(0,19).box(136,26,200).union(w0.sketch().push([(36,-21)]).circle(11).circle(9,mode='s').finalize().extrude(-55))