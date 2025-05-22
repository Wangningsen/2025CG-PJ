import cadquery as cq
w0=cq.Workplane('YZ',origin=(-12,0,0))
w1=cq.Workplane('ZX',origin=(0,12,0))
r=w0.sketch().push([(15.5,-21)]).rect(37,84).push([(9.5,9)]).rect(19,8,mode='s').push([(22,-7)]).circle(7,mode='s').push([(25,-38)]).circle(7,mode='s').finalize().extrude(-26).union(w0.sketch().segment((-100,31),(-64,-43)).segment((-8,-16)).segment((-8,-49)).segment((39,-49)).segment((39,6)).segment((-4,6)).segment((-32,64)).close().assemble().finalize().extrude(64)).union(w1.workplane(offset=88/2).moveTo(-55,-33).box(18,38,88))