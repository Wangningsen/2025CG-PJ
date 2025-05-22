import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,41))
w1=cq.Workplane('XY',origin=(0,0,56))
r=w0.sketch().arc((53,85),(-79,-62),(94,35)).segment((94,85)).close().assemble().push([(22,-11)]).circle(71,mode='s').push([(-13,3)]).circle(14).finalize().extrude(-48).union(w1.sketch().segment((-64,61),(55,61)).segment((55,91)).segment((26,91)).segment((-64,91)).close().assemble().finalize().extrude(-112))