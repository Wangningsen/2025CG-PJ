import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-11,0))
w1=cq.Workplane('YZ',origin=(-96,0,0))
r=w0.sketch().arc((-5,36),(-93,-58),(37,-45)).arc((91,-19),(91,41)).segment((91,97)).arc((81,90),(71,86)).segment((71,58)).arc((26,62),(-5,36)).assemble().finalize().extrude(43).union(w1.sketch().push([(-4,-72.5)]).rect(56,19).push([(-24,-76)]).circle(5,mode='s').push([(-4,-72)]).circle(3,mode='s').finalize().extrude(137))