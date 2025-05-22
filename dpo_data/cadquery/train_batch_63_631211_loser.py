import cadquery as cq
w0=cq.Workplane('YZ',origin=(-79,0,0))
r=w0.workplane(offset=-21/2).cylinder(21,17).union(w0.sketch().circle(29).push([(27,5)]).rect(4,6,mode='s').finalize().extrude(179))