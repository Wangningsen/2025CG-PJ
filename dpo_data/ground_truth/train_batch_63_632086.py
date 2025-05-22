import cadquery as cq
w0=cq.Workplane('YZ',origin=(66,0,0))
w1=cq.Workplane('ZX',origin=(0,28,0))
r=w0.sketch().push([(10.5,-8.5)]).rect(179,165).push([(20.5,-43.5)]).rect(9,35,mode='s').finalize().extrude(-138).union(w0.sketch().push([(11,-8)]).circle(89).circle(53,mode='s').push([(10.5,-8.5)]).rect(91,19).finalize().extrude(5)).union(w1.sketch().segment((-33,-23),(97,-23)).arc((31,23),(-33,-23)).assemble().finalize().extrude(-128))