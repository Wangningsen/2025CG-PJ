import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-37,0))
r=w0.sketch().push([(-14,-38)]).circle(42).reset().face(w0.sketch().segment((12,-20),(34,-20)).segment((34,0)).segment((14,0)).arc((53,-13),(12,-20)).assemble()).push([(70,-76)]).circle(24).push([(61,-73)]).circle(4,mode='s').finalize().extrude(16).union(w0.workplane(offset=74/2).moveTo(-64,70).cylinder(74,30))