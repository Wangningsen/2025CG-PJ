import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,5,0))
w1=cq.Workplane('YZ',origin=(0,0,0))
r=w0.sketch().push([(-42,3)]).circle(8).push([(-41,-3)]).circle(1,mode='s').push([(46.5,76.5)]).rect(59,47).finalize().extrude(-51).union(w0.sketch().arc((-53,-21),(-61,-8),(-50,-19)).arc((-49,-20),(-49,-21)).arc((-65,-2),(-52,-23)).arc((-52,-22),(-53,-21)).assemble().finalize().extrude(-37)).union(w1.workplane(offset=-100/2).moveTo(26,-57).cylinder(100,19))