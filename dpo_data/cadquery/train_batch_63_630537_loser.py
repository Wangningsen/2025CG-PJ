import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-35,0))
r=w0.sketch().push([(-84.5,-23.5)]).rect(31,115).push([(-7,52)]).circle(29).push([(-6,14)]).circle(5).push([(83,-51)]).circle(17).finalize().extrude(71)