import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,68,0))
r=w0.sketch().circle(27).push([(19,-5)]).circle(6,mode='s').finalize().extrude(-135).union(w0.workplane(offset=-116/2).box(150,200,116))