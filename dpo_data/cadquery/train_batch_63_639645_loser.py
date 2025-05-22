import cadquery as cq
w0=cq.Workplane('YZ',origin=(27,0,0))
r=w0.workplane(offset=-119/2).box(114,200,119).union(w0.sketch().circle(20).push([(0,10)]).circle(8,mode='s').finalize().extrude(65))