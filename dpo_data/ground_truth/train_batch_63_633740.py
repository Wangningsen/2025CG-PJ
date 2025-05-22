import cadquery as cq
w0=cq.Workplane('YZ',origin=(-41,0,0))
w1=cq.Workplane('ZX',origin=(0,-34,0))
r=w0.workplane(offset=7/2).moveTo(8,23).cylinder(7,15).union(w0.sketch().arc((-6,-4),(62,-92),(59,18)).arc((64,40),(57,62)).segment((57,45)).segment((46,45)).segment((55,35)).segment((38,20)).arc((23,17),(11,11)).segment((1,23)).segment((28,45)).segment((21,45)).segment((21,81)).segment((38,81)).arc((-27,59),(-6,-4)).assemble().finalize().extrude(82)).union(w1.sketch().push([(73.5,-3.5)]).rect(45,51).push([(74,-23)]).circle(4,mode='s').finalize().extrude(-66))