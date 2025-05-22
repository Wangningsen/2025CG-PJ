import cadquery as cq
w0=cq.Workplane('YZ',origin=(100,0,0))
r=w0.sketch().push([(-70,-60)]).circle(4).circle(3,mode='s').finalize().extrude(-200).union(w0.workplane(offset=-76/2).moveTo(33,51).box(84,28,76))