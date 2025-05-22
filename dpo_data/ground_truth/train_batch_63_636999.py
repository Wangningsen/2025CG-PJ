import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,55))
r=w0.workplane(offset=-149/2).moveTo(-71.5,61).box(57,64,149).union(w0.sketch().push([(91,-30)]).rect(18,126).push([(93,6)]).circle(7,mode='s').finalize().extrude(39))