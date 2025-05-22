import cadquery as cq
w0=cq.Workplane('YZ',origin=(39,0,0))
w1=cq.Workplane('ZX',origin=(0,4,0))
r=w0.sketch().arc((-30,53),(-47,-63),(61,-16)).arc((52,65),(-30,53)).assemble().finalize().extrude(61).union(w1.sketch().push([(53,-82)]).circle(18).push([(58,-74)]).circle(7,mode='s').finalize().extrude(-79))