import cadquery as cq
w0=cq.Workplane('YZ',origin=(10,0,0))
r=w0.workplane(offset=-50/2).moveTo(-18,71).box(56,58,50).union(w0.workplane(offset=23/2).moveTo(27,-68).cylinder(23,32)).union(w0.sketch().push([(-55,12)]).circle(4).circle(1,mode='s').finalize().extrude(29))