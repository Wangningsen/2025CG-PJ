import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-2,0))
r=w0.sketch().segment((-68,-22),(-66,-24)).segment((-66,-28)).segment((-65,-28)).segment((-7,-79)).segment((68,6)).segment((-18,80)).segment((-66,23)).segment((-66,-18)).close().assemble().push([(-12,0)]).circle(27,mode='s').finalize().extrude(-98).union(w0.workplane(offset=102/2).moveTo(-11.5,0).box(105,60,102))