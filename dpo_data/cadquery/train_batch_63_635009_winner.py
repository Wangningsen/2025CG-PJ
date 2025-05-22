import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-2,0))
w1=cq.Workplane('YZ',origin=(47,0,0))
r=w0.sketch().push([(62.5,24)]).rect(23,38).push([(63,24)]).circle(2,mode='s').finalize().extrude(47).union(w0.workplane(offset=85/2).moveTo(-82,-29).cylinder(85,18)).union(w1.sketch().segment((-12,-21),(23,-21)).segment((23,-10)).arc((27,-2),(23,9)).segment((23,57)).segment((2,57)).arc((-79,75),(-12,25)).close().assemble().finalize().extrude(-89))