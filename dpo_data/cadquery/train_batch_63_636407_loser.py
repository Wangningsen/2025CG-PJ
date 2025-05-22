import cadquery as cq
w0=cq.Workplane('YZ',origin=(34,0,0))
w1=cq.Workplane('XY',origin=(0,0,-82))
r=w0.sketch().arc((-36,15),(-20,-88),(60,-36)).arc((64,84),(-36,15)).assemble().finalize().extrude(66).union(w1.sketch().push([(-35,-34)]).circle(65).push([(-23.5,-89)]).rect(13,8,mode='s').finalize().extrude(150))