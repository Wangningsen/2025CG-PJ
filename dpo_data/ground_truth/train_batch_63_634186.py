import cadquery as cq
w0=cq.Workplane('YZ',origin=(33,0,0))
r=w0.sketch().circle(29).push([(-12,-9)]).circle(12,mode='s').finalize().extrude(-133).union(w0.sketch().circle(87).push([(-24,45)]).circle(23,mode='s').finalize().extrude(67))