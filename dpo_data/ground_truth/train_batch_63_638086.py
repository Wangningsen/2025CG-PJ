import cadquery as cq
w0=cq.Workplane('YZ',origin=(-41,0,0))
w1=cq.Workplane('ZX',origin=(0,-59,0))
r=w0.sketch().push([(15,-56)]).circle(44).push([(54,-53.5)]).rect(2,5,mode='s').finalize().extrude(-55).union(w1.sketch().arc((-24,19),(-58,-45),(2,-85)).arc((80,-71),(93,7)).arc((43,96),(-24,19)).assemble().finalize().extrude(34))