import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,22,0))
w1=cq.Workplane('ZX',origin=(0,47,0))
r=w0.workplane(offset=-69/2).moveTo(-7,-20).cylinder(69,30).union(w0.sketch().arc((-30,-7),(-31,-30),(-13,-45)).arc((-26,-28),(-30,-7)).assemble().finalize().extrude(17)).union(w0.workplane(offset=19/2).moveTo(29,-84).cylinder(19,16)).union(w1.sketch().push([(-23,63.5)]).rect(44,73).push([(-23,63)]).circle(14,mode='s').finalize().extrude(-8))