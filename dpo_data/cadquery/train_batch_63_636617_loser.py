import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,4,0))
w1=cq.Workplane('YZ',origin=(39,0,0))
r=w0.sketch().push([(52,-82)]).circle(18).push([(59,-79)]).circle(4,mode='s').finalize().extrude(-79).union(w1.sketch().arc((-30,53),(-45,-64),(62,-16)).arc((52,66),(-30,53)).assemble().finalize().extrude(61))