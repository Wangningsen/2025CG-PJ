import cadquery as cq
w0=cq.Workplane('YZ',origin=(-12,0,0))
w1=cq.Workplane('YZ',origin=(-52,0,0))
r=w0.sketch().push([(15.5,-21)]).rect(37,84).push([(15,-21)]).circle(14,mode='s').push([(15.5,13)]).rect(25,16,mode='s').finalize().extrude(-26).union(w0.sketch().segment((-100,31),(-64,-43)).segment((-8,-16)).segment((-8,-49)).segment((39,-49)).segment((39,6)).segment((-4,6)).segment((-32,64)).close().assemble().finalize().extrude(64)).union(w1.workplane(offset=38/2).moveTo(48.5,-55).box(103,18,38))