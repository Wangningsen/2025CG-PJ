import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,31,0))
w1=cq.Workplane('YZ',origin=(33,0,0))
r=w0.sketch().arc((-15,-78),(66,-65),(0,-14)).arc((-66,-31),(-15,-78)).assemble().push([(-34,73)]).circle(27).push([(13,33.5)]).rect(50,67).finalize().extrude(-88).union(w1.sketch().segment((-22,7),(57,7)).segment((57,39)).segment((-10,39)).segment((-10,38)).segment((-22,38)).close().assemble().finalize().extrude(40))