import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-27))
r=w0.sketch().arc((-43,-31),(-21,1),(-26,-38)).arc((26,61),(-43,-31)).assemble().finalize().extrude(-4).union(w0.sketch().segment((-99,-86),(-49,-86)).arc((3,-100),(54,-82)).segment((54,-86)).segment((99,-86)).segment((99,100)).segment((-99,100)).close().assemble().push([(2,-12)]).circle(54,mode='s').finalize().extrude(58))