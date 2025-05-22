import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-37,0))
w1=cq.Workplane('YZ',origin=(-90,0,0))
r=w0.sketch().segment((-98,-100),(-62,-100)).segment((-62,-30)).arc((-24,-55),(21,-40)).segment((22,-46)).segment((50,-39)).segment((47,-22)).arc((67,-10),(79,10)).segment((79,23)).segment((83,23)).arc((67,98),(12,44)).segment((0,15)).arc((-38,20),(-64,-8)).segment((-98,-8)).close().assemble().finalize().extrude(94).union(w0.workplane(offset=110/2).moveTo(2,-17).cylinder(110,24)).union(w1.workplane(offset=96/2).moveTo(-47.5,-50.5).box(51,57,96))