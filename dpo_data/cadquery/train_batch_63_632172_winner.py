import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-23,0))
w1=cq.Workplane('YZ',origin=(-32,0,0))
r=w0.sketch().push([(-65,-53)]).rect(70,8).push([(-35,24)]).circle(34).push([(-43,-25.5)]).rect(4,21).push([(72,-21)]).circle(28).finalize().extrude(51).union(w1.workplane(offset=19/2).moveTo(-2,7).box(54,10,19))