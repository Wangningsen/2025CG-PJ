import cadquery as cq
w0=cq.Workplane('YZ',origin=(12,0,0))
r=w0.workplane(offset=-112/2).moveTo(-86,83).cylinder(112,8).union(w0.sketch().push([(62.5,-85.5)]).rect(63,11).push([(81,-86)]).circle(3,mode='s').finalize().extrude(88))