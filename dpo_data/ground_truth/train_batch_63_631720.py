import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-5))
r=w0.sketch().push([(-54,-64.5)]).rect(24,33).push([(-54,-64)]).circle(6,mode='s').finalize().extrude(-95).union(w0.workplane(offset=-32/2).moveTo(4,-25).cylinder(32,41)).union(w0.workplane(offset=105/2).moveTo(20,51.5).box(92,59,105))