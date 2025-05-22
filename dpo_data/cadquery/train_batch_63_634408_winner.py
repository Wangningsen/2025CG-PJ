import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-21,0))
w1=cq.Workplane('ZX',origin=(0,-12,0))
r=w0.sketch().push([(-12,60)]).rect(96,80).reset().face(w0.sketch().segment((-52,54),(-20,54)).segment((-20,48)).segment((-4,48)).segment((-4,54)).segment((29,54)).segment((29,66)).segment((-4,66)).segment((-4,72)).segment((-20,72)).segment((-20,66)).segment((-52,66)).close().assemble(),mode='s').push([(59,-91.5)]).rect(2,17).finalize().extrude(83).union(w1.sketch().segment((-41,-100),(53,-100)).arc((51,-92),(53,-83)).segment((-41,-83)).close().assemble().finalize().extrude(-49))