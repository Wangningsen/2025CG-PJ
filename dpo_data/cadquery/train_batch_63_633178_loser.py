import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-68,0))
r=w0.sketch().push([(-14.5,-2.5)]).rect(115,195).push([(-65,-14)]).circle(3,mode='s').finalize().extrude(-11).union(w0.sketch().arc((38,100),(47,68),(72,72)).arc((54,84),(38,100)).assemble().finalize().extrude(147))