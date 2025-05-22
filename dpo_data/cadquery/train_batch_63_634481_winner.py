import cadquery as cq
w0=cq.Workplane('YZ',origin=(-8,0,0))
r=w0.sketch().arc((-18,83),(-46,18),(14,-20)).arc((71,9),(59,70)).arc((28,100),(-12,85)).arc((-15,83),(-18,83)).assemble().finalize().extrude(13).union(w0.sketch().push([(-6,-31)]).circle(69).circle(5,mode='s').finalize().extrude(16))