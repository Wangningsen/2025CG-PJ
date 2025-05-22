import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-2,0))
w1=cq.Workplane('YZ',origin=(47,0,0))
r=w0.sketch().push([(62.5,24)]).rect(23,38).push([(64,32)]).circle(7,mode='s').finalize().extrude(47).union(w0.workplane(offset=85/2).moveTo(-82,-29).cylinder(85,18)).union(w1.sketch().segment((-12,-21),(23,-21)).segment((23,-14)).arc((27,-1),(23,12)).segment((23,57)).segment((3,57)).arc((-78,76),(-12,25)).close().assemble().finalize().extrude(-89))