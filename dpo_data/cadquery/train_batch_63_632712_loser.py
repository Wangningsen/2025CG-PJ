import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-9))
r=w0.workplane(offset=-65/2).moveTo(-95,68.5).box(8,59,65).union(w0.sketch().push([(58.5,-32.5)]).rect(83,131).push([(58,-33)]).circle(11,mode='s').finalize().extrude(83))