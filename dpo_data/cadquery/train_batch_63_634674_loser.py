import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-41))
w1=cq.Workplane('XY',origin=(0,0,-42))
r=w0.sketch().segment((-48,-22),(-18,-40)).segment((48,22)).segment((18,40)).close().assemble().finalize().extrude(62).union(w1.workplane(offset=84/2).box(84,200,84))