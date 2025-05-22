import cadquery as cq
w0=cq.Workplane('YZ',origin=(100,0,0))
r=w0.sketch().circle(29).push([(-12,-10)]).circle(13,mode='s').finalize().extrude(-200).union(w0.sketch().circle(87).push([(-24,45)]).circle(23,mode='s').finalize().extrude(-67))