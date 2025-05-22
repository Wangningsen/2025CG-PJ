import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-75))
r=w0.sketch().push([(-21.5,-10.5)]).rect(157,39).push([(-23,-10)]).circle(17,mode='s').finalize().extrude(140).union(w0.workplane(offset=151/2).moveTo(61.5,0).box(77,102,151))