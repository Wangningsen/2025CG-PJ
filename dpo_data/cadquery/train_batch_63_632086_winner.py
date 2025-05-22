import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,22,0))
w1=cq.Workplane('YZ',origin=(66,0,0))
r=w0.sketch().segment((-21,-23),(97,-22)).arc((38,19),(-21,-23)).assemble().finalize().extrude(-122).union(w0.sketch().segment((-97,68),(-68,68)).arc((-74,71),(-80,71)).arc((-89,70),(-97,68)).assemble().finalize().extrude(-13)).union(w1.sketch().push([(10.5,-8.5)]).rect(179,165).push([(20.5,-43.5)]).rect(11,35,mode='s').finalize().extrude(-138))