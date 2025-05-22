import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-2,0))
w1=cq.Workplane('YZ',origin=(47,0,0))
r=w0.sketch().push([(62.5,22.5)]).rect(23,41).push([(63,23)]).circle(2,mode='s').push([(67,28)]).rect(10,12,mode='s').finalize().extrude(47).union(w0.workplane(offset=85/2).moveTo(-82,-29).cylinder(85,18)).union(w1.sketch().segment((-13,27),(-12,27)).segment((-12,-21)).segment((23,-21)).segment((23,-13)).arc((27,-2),(23,8)).segment((23,57)).segment((3,57)).arc((-77,78),(-13,27)).assemble().finalize().extrude(-89))