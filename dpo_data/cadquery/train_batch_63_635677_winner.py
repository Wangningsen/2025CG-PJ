import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,30))
r=w0.sketch().segment((-55,-16),(-34,-16)).segment((-34,-60)).segment((32,-60)).segment((32,-16)).segment((55,-16)).segment((55,16)).segment((32,16)).segment((32,60)).segment((-34,60)).segment((-34,16)).segment((-55,16)).close().assemble().finalize().extrude(-130).union(w0.workplane(offset=70/2).moveTo(-24.5,0).box(15,76,70))